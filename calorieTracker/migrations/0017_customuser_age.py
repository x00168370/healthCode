# Generated by Django 4.2 on 2023-04-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0016_remove_profile_all_meals_remove_profile_meal_eaten_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.DateField(blank=True, null=True),
        ),
    ]
