# Generated by Django 2.2.24 on 2021-08-28 03:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0021_auto_20210828_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chardata2',
            name='myArmorHead',
        ),
        migrations.RemoveField(
            model_name='chardata2',
            name='myArmorLower',
        ),
        migrations.RemoveField(
            model_name='chardata2',
            name='myArmorUpper',
        ),
        migrations.RemoveField(
            model_name='chardata2',
            name='myWeapon',
        ),
        migrations.DeleteModel(
            name='CharData',
        ),
        migrations.DeleteModel(
            name='CharData2',
        ),
    ]