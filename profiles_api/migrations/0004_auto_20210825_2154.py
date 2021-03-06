# Generated by Django 2.2 on 2021-08-25 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0003_profileprefrence'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileprefrence',
            old_name='changed_on',
            new_name='modified_on',
        ),
        migrations.CreateModel(
            name='articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('IMAGE', models.URLField()),
                ('user_info', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.profilePrefrence')),
            ],
        ),
    ]
