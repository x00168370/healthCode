# Generated by Django 4.1.3 on 2023-02-14 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='link',
        ),
    ]
