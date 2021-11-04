# Generated by Django 2.2.24 on 2021-10-29 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0036_monsterlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='monsterlog',
            name='attackPower',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='攻撃力'),
        ),
        migrations.AddField(
            model_name='monsterlog',
            name='battle',
            field=models.CharField(default='攻撃', max_length=50, verbose_name='攻防'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='monsterlog',
            name='damegeHp',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='ダメージ'),
        ),
        migrations.AddField(
            model_name='monsterlog',
            name='hp',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='ＨＰ'),
        ),
        migrations.AddField(
            model_name='monsterlog',
            name='name',
            field=models.CharField(default='モンスターＡ', max_length=50, verbose_name='モンスター名'),
            preserve_default=False,
        ),
    ]