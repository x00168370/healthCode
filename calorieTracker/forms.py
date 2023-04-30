from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import *

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields =  ('username', 'email', 'age',  'gender','height', 'goal_weight', 'current_weight', 'weight_goal')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'age', 'gender', 'height','goal_weight', 'current_weight', 'weight_goal')

class MealForm(ModelForm):
    class Meta:
        model = Meal
        fields = "__all__"

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = "__all__"
