# Generated by Django 4.1.3 on 2023-03-09 00:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0005_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='height',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='weight',
            field=models.FloatField(),
        ),
        migrations.CreateModel(
            name='Bmi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('bmi', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]