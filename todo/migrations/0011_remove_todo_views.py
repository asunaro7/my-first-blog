# Generated by Django 2.2.24 on 2021-08-11 10:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_todo_views'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='views',
        ),
    ]
