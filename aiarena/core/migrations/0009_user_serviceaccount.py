# Generated by Django 2.1.7 on 2019-05-05 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_participant_resultant_elo'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='serviceaccount',
            field=models.BooleanField(default=0),
        ),
    ]