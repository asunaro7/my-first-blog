# Generated by Django 2.2.24 on 2021-07-21 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='created_at',
            new_name='createdat',
        ),
    ]