# Generated by Django 4.2.3 on 2023-07-06 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20230316_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='location',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新日'),
        ),
        migrations.AlterField(
            model_name='result',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='result',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新日'),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='作成日'),
        ),
        migrations.AlterField(
            model_name='sensors',
            name='updated_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='更新日'),
        ),
    ]
