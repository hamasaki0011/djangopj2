# Generated by Django 3.2.17 on 2023-02-27 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'プロフィール', 'verbose_name_plural': 'プロフィール一覧'},
        ),
        migrations.AlterModelTable(
            name='profile',
            table='profile',
        ),
    ]