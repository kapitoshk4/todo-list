# Generated by Django 5.0.6 on 2024-05-19 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_deadline'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['completed', '-created_at']},
        ),
        migrations.RemoveField(
            model_name='todo',
            name='status',
        ),
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]
