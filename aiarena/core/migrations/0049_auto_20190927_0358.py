# Generated by Django 2.1.7 on 2019-09-26 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_auto_20190927_0318'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Participant',
            new_name='Participation',
        ),
    ]