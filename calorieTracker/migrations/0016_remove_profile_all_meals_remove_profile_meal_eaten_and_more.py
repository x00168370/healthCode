# Generated by Django 4.2 on 2023-04-27 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0015_remove_customuser_phone_customuser_height'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='all_meals',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='meal_eaten',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='PostMeal',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
