from django.urls import reverse_lazy

from django.views.generic import TemplateView, DetailView, CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView

from django.views.decorators.csrf import csrf_protect

from .models import *
from .forms import *
from .filters import *

from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Sum

from django.views.decorators.csrf import csrf_exempt

from datetime import date, datetime, timedelta, timezone

import requests
import json


# ****************** User Auth Start ******************
@csrf_protect
def signupView(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # or any other URL to redirect to after successful signup
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@csrf_protect
def signinView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('signup')
    else:
        form = AuthenticationForm()
        return render(request, 'registration/signin.html', {'form': form})


def signoutView(request):
    logout(request)
    return redirect('home')


class HomePageView(TemplateView):
    template_name = 'home.html'
# ****************** User Auth End ******************


def profile(request):
    user = request.user
    return render(request, 'profile.html', {'user': user})


def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance=request.user)
    
    return render(request, 'edit_profile.html', {'form': form})



# ****************** Exercise Views Start ******************
class ExerciseCreateView(LoginRequiredMixin, CreateView):
    model = Exercise
    fields = ["activity", "duration", "weight"]
    success_url = reverse_lazy("home")
    template_name = 'exercise.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExerciseListView(LoginRequiredMixin, ListView):
    model = Exercise
    template_name = 'exercise_list.html'


    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exercises = context['object_list']
        today = date.today()

        # Daily Exercise Calories Burned
        daily_calories_burned = sum(
            exercise.calories_burned for exercise in exercises if exercise.date.date() == today)
        context['daily_calories_burned'] = daily_calories_burned

        # Weekly Workout Duration
        daily_workout_duration = sum(
            exercise.calories_burned for exercise in exercises if exercise.date.date() == today)
        context['daily_workout_duration'] = daily_workout_duration

        # Daily Exercise Calories Burned
        weekly_calories_burned = sum(
            exercise.calories_burned for exercise in exercises
            if (today - timedelta(days=7)) <= exercise.date.date() <= today)
        context['weekly_calories_burned'] = weekly_calories_burned

        # Weekly Workout Duration
        weekly_workout_duration = sum(
            exercise.duration for exercise in exercises
            if (today - timedelta(days=7)) <= exercise.date.date() <= today)
        context['weekly_workout_duration'] = weekly_workout_duration

        # Check if user has entered a exercise today
        has_entered_exercise_today = any(
            exercise.date.date() == today for exercise in exercises)
        context['has_entered_exercise_today'] = has_entered_exercise_today


        return context


class ExerciseDetailView(DetailView):
    model = Exercise
    template_name = 'exercise_detail.html'


class ExerciseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Exercise
    fields = ["activity", "duration", "weight"]
    template_name = 'exercise_edit.html'

    def get_success_url(self):
        return reverse_lazy("home")

    def test_func(self):
        exercise = self.get_object()
        return self.request.user == exercise.user


class ExerciseDeleteView(DeleteView):
    model = Exercise
    template_name = 'exercise_delete.html'
    success_url = reverse_lazy("home")

    def test_func(self):
        exercise = self.get_object()
        return self.request.user == exercise.user
# ****************** Exercise Views End ******************





# ****************** Meal Views Start ******************
class MealCreateView(CreateView):

    model = Meal
    fields = ["category", "name", "fat",
              "protein", "carbs", "quantity", "calories"]
    template_name = 'meal.html'
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MealListView(ListView):
    model = Meal
    template_name = 'meal_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meals = context['object_list']
        today = datetime.now().date()

        # Daily calories consumed
        daily_calories = sum(
            meal.calories for meal in meals if meal.date.date() == today)
        context['daily_calories'] = daily_calories

        # Weekly calories consumed
        weekly_calories = sum(
            meal.calories for meal in meals
            if (today - timedelta(days=7)) <= meal.date.date() <= today)
        context['weekly_calories'] = weekly_calories

        # Check if user has entered a meal for today
        has_entered_meal_today = any(
            meal.date.date() == today for meal in meals)
        context['has_entered_meal_today'] = has_entered_meal_today

        return context


class MealDetailView(DetailView):
    model = Meal
    template_name = "meal_detail.html"


class MealUpdateView(UpdateView):
    model = Meal
    fields = ["category", "name", "fat",
              "protein", "carbs", "quantity", "calories"]
    template_name = "meal_edit.html"

    def get_success_url(self):
        return reverse_lazy("home")

    def test_func(self):
        meal = self.get_object()
        return self.request.user == meal.user


class MealDeleteView(DeleteView):

    model = Meal
    template_name = 'meal_delete.html'
    success_url = reverse_lazy("home")

    def test_func(self):
        meal = self.get_object()
        return self.request.user == meal.user
# ****************** Meal Views End ******************


# ****************** CONSUMING APIS ******************


# ****************** Meal Search API Start  ******************
def meal_search(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'NmUuLV/hyQMYCirDx3ErkA==HbEVEULM8UPuDDfW'})
        try:
            meal_api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            meal_api = "oops! There was an error"
            print(e)
        return render(request, 'meal_search.html', {'meal_api': meal_api})
    else:
        return render(request, 'meal_search.html', {'query': 'Enter a valid query'})
# ****************** Meal Search API End ******************


# ****************** Muscle Search API Start ******************
def muscle_search(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/exercises?muscle='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'NmUuLV/hyQMYCirDx3ErkA==HbEVEULM8UPuDDfW'})
        try:
            ex_api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            ex_api = 'Error'
            print(e)
        return render(request, 'muscle_search.html', {'ex_api': ex_api})
    else:
        return render(request, 'muscle_search.html', {'query': 'Search Exercise by muscle group'})
# ****************** Muscle API End ******************
