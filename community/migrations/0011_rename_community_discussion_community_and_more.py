# Generated by Django 4.1.3 on 2023-04-18 11:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0010_discussion_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='Community',
            new_name='community',
        ),
        migrations.RemoveField(
            model_name='discussion',
            name='active',
        ),
        migrations.AddField(
            model_name='community',
            name='likes',
            field=models.ManyToManyField(related_name='community_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='content',
            field=models.TextField(),
        ),
    ]
