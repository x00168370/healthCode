# Generated by Django 4.1.3 on 2023-03-17 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_tags_alter_community_options_community_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discussion',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='discussion',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
