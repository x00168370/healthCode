from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views
from .views import *

app_name = "calorieTracker"

urlpatterns= [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),

    path('signup/', signupView, name='signup'),
    path('signin/', signinView, name='signin'),
    path('logout/', signoutView, name='logout'),

    path('profile/', profile, name='profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),


    path('exercise/', ExerciseCreateView.as_view(),name="exercise"),
    path('exercise_list/', ExerciseListView.as_view(), name="exercise_list"),
    path("<int:pk>/", ExerciseDetailView.as_view(),name="exercise_detail"),
    path("<int:pk>/exercise_edit/", ExerciseUpdateView.as_view(), name="exercise_edit"),
    path("<int:pk>/exercise_delete/", ExerciseDeleteView.as_view(), name="exercise_delete"),


    path('meal/', MealCreateView.as_view(),name="meal"),
    path('meal_list/', MealListView.as_view(), name="meal_list"),
    path("<int:pk>/", MealDetailView.as_view(), name="meal_detail"),
    path("<int:pk>/edit/", MealUpdateView.as_view(), name="meal_edit"),
    path("<int:pk>/delete/", MealDeleteView.as_view(), name="meal_delete"),

    path('search/', meal_search, name='meal_search'),
    path('muscle_search/', muscle_search, name='muscle_search'),


    


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

