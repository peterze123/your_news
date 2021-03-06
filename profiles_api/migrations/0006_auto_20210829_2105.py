# Generated by Django 2.2 on 2021-08-29 21:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles_api', '0005_auto_20210825_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='profileFeed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('modified_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='articles',
            name='user_info',
        ),
        migrations.AddField(
            model_name='userinfo',
            name='preference',
            field=models.CharField(choices=[('business', 'business'), ('entertainment', 'entertainment'), ('general', 'general'), ('health', 'health'), ('science', 'science'), ('sports', 'sports'), ('technology', 'technology')], default='general', max_length=13),
        ),
        migrations.DeleteModel(
            name='profilePrefrence',
        ),
        migrations.AddField(
            model_name='profilefeed',
            name='article_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles_api.articles'),
        ),
        migrations.AddField(
            model_name='profilefeed',
            name='user_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
