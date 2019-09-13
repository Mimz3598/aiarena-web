# Generated by Django 2.1.7 on 2019-09-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_auto_20190907_0615'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='patreon_level',
            field=models.CharField(choices=[('None', 'None'), ('Bronze', 'Bronze'), ('Silver', 'Silver'), ('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Diamond', 'Diamond')], default='None', max_length=16),
        ),
    ]