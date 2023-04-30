# Generated by Django 4.1.3 on 2023-03-17 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0006_alter_profile_height_alter_profile_weight_bmi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bmi',
            name='height',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='bmi',
            name='weight',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
