# Generated by Django 4.2 on 2023-04-27 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0017_customuser_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='quantity',
        ),
    ]