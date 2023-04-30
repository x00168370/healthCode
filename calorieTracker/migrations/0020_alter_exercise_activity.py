# Generated by Django 4.2 on 2023-04-30 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorieTracker', '0019_meal_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='activity',
            field=models.CharField(choices=[('running', 'Running'), ('jogging', 'Jogging'), ('walking', 'Walking'), ('skipping', 'Skipping'), ('skiing', 'Skiing'), ('cycling', 'Cycling'), ('dance', 'Dance'), ('squats', 'Squats'), ('pushups', 'Pushups'), ('sit ups', 'Sit ups'), ('pull ups', 'Pull ups'), ('hiking', 'Hiking'), ('lunges', 'Lunges'), ('crunches', 'Crunches'), ('basketball', 'Basketball'), ('Volleyball', 'Volleyball'), ('Football', 'Football'), ('circuit training', 'Circuit training'), ('tennis', 'Tennis'), ('boxing', 'Boxing'), ('Weight lifting (moderate effort)', 'Weight lifting (moderate effort)'), ('Weight lifting (vigorous effort)', 'Weight lifting (vigorous effort)'), ('Elliptical trainer (moderate effort)', 'Elliptical trainer (moderate effort)'), ('Elliptical trainer (vigorous effort)', 'Elliptical trainer (vigorous effort)'), ('Rowing machine (moderate effort)', 'Rowing machine (moderate effort)'), ('Rowing machine (vigorous effort)', 'Rowing machine (vigorous effort)'), ('Stair climbing (moderate effort)', 'Stair climbing (moderate effort)'), ('Stair climbing (vigorous effort)', 'Stair climbing (vigorous effort)'), ('Skipping (moderate effort)', 'Skipping (moderate effort)'), ('Skipping (vigorous effort)', 'Skipping (vigorous effort)'), ('Swimming (moderate effort)', 'Swimming (moderate effort)'), ('Rock climbing (moderate effort)', 'Rock climbing (moderate effort)'), ('Martial arts (e.g. karate, judo)', 'Martial arts (e.g. karate, judo)'), ('Aerobics (low impact)', 'Aerobics (low impact)'), ('Aerobics (high impact)', 'Aerobics (high impact)'), ('pilates', 'Pilates'), ('Pilates (advanced)', 'Pilates (advanced)'), ('yoga', 'Yoga'), ('Yoga (advanced)', 'Yoga (advanced)'), ('Tai chi', 'Tai chi')], max_length=100),
        ),
    ]