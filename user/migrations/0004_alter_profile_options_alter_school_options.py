# Generated by Django 5.0.6 on 2024-05-17 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_profile_followers_alter_profile_following'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name_plural': 'KULLANICI ÖZELLİKLERİ EKLEME'},
        ),
        migrations.AlterModelOptions(
            name='school',
            options={'verbose_name_plural': 'KULLANICIYA OKUL EKLEME'},
        ),
    ]