# Generated by Django 2.1.7 on 2019-05-13 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_bot_in_match'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='serviceaccount',
            new_name='service_account',
        ),
        migrations.AlterField(
            model_name='user',
            name='service_account',
            field=models.BooleanField(default=True),
        ),
    ]
