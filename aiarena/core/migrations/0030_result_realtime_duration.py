# Generated by Django 2.1.7 on 2019-07-17 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_auto_20190718_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='realtime_duration',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
