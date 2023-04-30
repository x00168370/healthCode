from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, User
from django.db.models import Sum
from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone
import datetime
import requests
# Create your models here.


class CustomUser(AbstractUser):
    age = models.DateField(blank=True, null=True)
    goal_weight = models.FloatField(null=True, blank=True)
    current_weight = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight_goal = models.CharField(
        max_length=20,
        choices=[('lose', 'Lose Weight'), ('gain', 'Gain Weight'), ('maintain', 'Maintain Weight')],
        null=True, blank=True
    )
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female')],
        null=True, blank=True
    )

    def dob(self):
        import datetime
        return int((datetime.date.today() - self.age).days / 365.25  )





class Meal(models.Model):

    Categories = (
        ('Breakfast', 'Breakfast'),
        ('Lunch', 'Lunch'),
        ('Snacks', 'Snacks'),
        ('Dinner', 'Dinner')
    )

    name = models.CharField(max_length=100, null=True)
    date = models.DateTimeField(auto_now_add=True)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    category = models.CharField(choices=Categories, max_length=100)
    quantity = models.IntegerField()
    calories = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('meal_detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['-date']



# used to log in exercise to exercise log

class Exercise(models.Model):
    Activities = (
        ('running', 'Running'),
        ('jogging', 'Jogging'),
        ('walking', 'Walking'),
        ('skipping', 'Skipping'),
        ('skiing', 'Skiing'),
        ('cycling', 'Cycling'),
        ('dance', 'Dance'),
        ('squats', 'Squats'),
        ('pushups', 'Pushups'),
        ('sit ups', 'Sit ups'),
        ('pull ups', 'Pull ups'),
        ('hiking', 'Hiking'),
        ('lunges', 'Lunges'),
        ('crunches', 'Crunches'),
        ('basketball', 'Basketball'),
        ('Volleyball', 'Volleyball'),
        ('Football', 'Football'),
        ('circuit training', 'Circuit training'),
        ('tennis', 'Tennis'),
        ('boxing', 'Boxing'),
        ('Weight lifting (moderate effort)', 'Weight lifting (moderate effort)'),
        ('Weight lifting (vigorous effort)', 'Weight lifting (vigorous effort)'),
        ('Elliptical trainer (moderate effort)', 'Elliptical trainer (moderate effort)'),
        ('Elliptical trainer (vigorous effort)', 'Elliptical trainer (vigorous effort)'),
        ('Rowing machine (moderate effort)', 'Rowing machine (moderate effort)'),
        ('Rowing machine (vigorous effort)', 'Rowing machine (vigorous effort)'),
        ('Stair climbing (moderate effort)', 'Stair climbing (moderate effort)'),
        ('Stair climbing (vigorous effort)', 'Stair climbing (vigorous effort)'),
        ('Skipping (moderate effort)', 'Skipping (moderate effort)'),
        ('Skipping (vigorous effort)', 'Skipping (vigorous effort)'),
        ('Swimming (moderate effort)', 'Swimming (moderate effort)'),
        ('Rock climbing (moderate effort)', 'Rock climbing (moderate effort)'),
        ('Martial arts (e.g. karate, judo)', 'Martial arts (e.g. karate, judo)'),
        ('Aerobics (low impact)', 'Aerobics (low impact)'),
        ('Aerobics (high impact)', 'Aerobics (high impact)'),
        ('pilates', 'Pilates'),
        ('Pilates (advanced)', 'Pilates (advanced)'),
        ('yoga', 'Yoga'),
        ('Yoga (advanced)', 'Yoga (advanced)'),
        ('Tai chi', 'Tai chi'),

    )

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    duration = models.IntegerField()
    weight = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    calories_burned = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    activity = models.CharField(choices=Activities, max_length=100)

    



    MET_VALUES = {
        'running': 8.0,
        'jogging': 7.0,
        'walking': 3.5,
        'skipping': 12.3,
        'skiing': 7.0,
        'cycling': 6.0,
        'skiing': 7.0,
        'dance': 6.0,
        'squats': 3.5,
        'pushups': 8.0,
        'sit ups': 3.8,
        'pull ups': 8.0,
        'hiking': 5.3,
        'lunges':  6.0,
        'crunches': 3.8,
        'circuit training': 8.0,
        'Weight lifting (moderate effort)': 5.0,
        'Weight lifting (vigorous effort)': 6.0,
        'Elliptical trainer (moderate effort)': 5.0,
        'Elliptical trainer (vigorous effort)': 8.0,
        'Rowing machine (moderate effort)': 6.0,
        'Rowing machine (vigorous effort)': 8.5,
        'Stair climbing (moderate effort)': 4.5,
        'Stair climbing (vigorous effort)': 8.0,
        'Skippig (moderate effort)': 10.0,
        'Skipping (vigorous effort)': 12.3,
        'Swimming (moderate effort)': 6.0,
        'Rock climbing (moderate effort)': 5.0,
        'basketball': 6.5,
        'Volleyball': 3.0,
        'Football': 8.0,
        'tennis': 8.0,
        'boxing': 9.0,
        'Martial arts (e.g. karate, judo)': 10.0,
        'Aerobics (low impact)': 5.0,
        'Aerobics (high impact)': 7.5,
        'Pilates (advanced)': 4.0,
        'pilates': 3,
        'Yoga (advanced)': 4.0,
        'Yoga': 2.5,
        'Tai chi': 2.5,
    }

    def __str__(self):
        return self.activity

    def get_absolute_url(self):
        return reverse('exercise_detail', args=[str(self.id)])
    
    class Meta:
        ordering = ['-date']
    
    def save(self, *args, **kwargs):
        if self.weight > 0:
            met = Exercise.MET_VALUES.get(self.activity.lower(), 0)
            if met > 0:
                calories_burned = met * self.weight * self.duration / 60
                self.calories_burned = round(calories_burned, 2)
        super().save(*args, **kwargs)
    



