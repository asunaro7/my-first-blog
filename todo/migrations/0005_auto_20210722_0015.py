# Generated by Django 2.2.24 on 2021-07-21 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20210721_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='deadline_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='締切日'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='作成日'),
        ),
    ]