# Generated by Django 2.2.23 on 2021-08-20 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='media'),
            preserve_default=False,
        ),
    ]
