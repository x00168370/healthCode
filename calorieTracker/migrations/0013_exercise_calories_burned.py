# Generated by Django 4.1.3 on 2023-04-26 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0012_remove_exercise_calories_burned_exercise_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='calories_burned',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]