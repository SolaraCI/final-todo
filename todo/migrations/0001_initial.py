# Generated by Django 4.2.7 on 2024-12-16 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('notes', models.TextField(blank=True, default='Tactics...', null=True)),
                ('in_progress', models.IntegerField(choices=[(1, 'Locker Room'), (2, 'Kick-off'), (3, 'Full-time')], default=1)),
                ('importance', models.IntegerField(choices=[(1, 'League 1'), (2, 'Championship'), (3, 'Premiership')], default=2)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
