# Generated by Django 4.1.3 on 2023-02-13 19:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('fat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('protein', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('carbs', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('category', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Snacks', 'Snacks'), ('Dinner', 'Dinner')], max_length=100)),
                ('quantity', models.IntegerField()),
                ('calories', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='uploadMeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumed', models.FloatField(default=0)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorieTracker.meal')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meal', models.ManyToManyField(to='calorieTracker.meal')),
                ('customer', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sets', models.PositiveIntegerField()),
                ('weight', models.PositiveIntegerField()),
                ('date_worked_out', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
