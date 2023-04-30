# Generated by Django 4.1.3 on 2023-03-09 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_remove_community_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='Community',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='discussions', to='community.community'),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='content',
            field=models.CharField(max_length=140),
        ),
    ]