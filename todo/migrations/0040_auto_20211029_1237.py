# Generated by Django 2.2.24 on 2021-10-29 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0039_auto_20211029_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='battlelog',
            name='pHp',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='プレイヤーＨＰ'),
        ),
        migrations.AddField(
            model_name='battlelog',
            name='pLevel',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='プレイヤーレベル'),
        ),
        migrations.AddField(
            model_name='battlelog',
            name='pMoney',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='プレイヤー持ち金'),
        ),
        migrations.AddField(
            model_name='battlelog',
            name='pName',
            field=models.CharField(default='勇者くん1', max_length=50, verbose_name='プレイヤー名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='battlelog',
            name='attackPower',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='モンスター攻撃力'),
        ),
        migrations.AlterField(
            model_name='battlelog',
            name='damegeHp',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='モンスターダメージ'),
        ),
        migrations.AlterField(
            model_name='battlelog',
            name='hp',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='モンスターＨＰ'),
        ),
    ]
