# Generated by Django 2.2 on 2021-08-21 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]
