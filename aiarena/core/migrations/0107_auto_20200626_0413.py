# Generated by Django 2.1.7 on 2020-06-25 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0106_relativeresult'),
    ]

    operations = [
        migrations.AddField(
            model_name='matchparticipation',
            name='match_log_has_been_cleaned',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='result',
            name='arenaclient_log_has_been_cleaned',
            field=models.BooleanField(default=False),
        ),
    ]
