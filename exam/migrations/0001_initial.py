# Generated by Django 5.0.6 on 2024-05-13 23:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Lessons', models.CharField(default=0, max_length=50, null=True, verbose_name='Ders Adı')),
                ('Exam_Title', models.CharField(default=0, max_length=50, null=True, verbose_name='Sınav Adı')),
                ('Question', models.TextField(blank=True, null=True, verbose_name='Soru')),
                ('Choice_A', models.TextField(blank=True, null=True, verbose_name='A Şıkkı')),
                ('Choice_B', models.TextField(blank=True, null=True, verbose_name='B Şıkkı')),
                ('Choice_C', models.TextField(blank=True, null=True, verbose_name='C Şıkkı')),
                ('Choice_D', models.TextField(blank=True, null=True, verbose_name='D Şıkkı')),
                ('Choice_E', models.TextField(blank=True, null=True, verbose_name='E Şıkkı')),
                ('Answer', models.TextField(blank=True, null=True, verbose_name='Cevap')),
                ('Classroom', models.CharField(default=0, max_length=10, null=True, verbose_name='Kaçıncı Sınıf Sorusu?')),
                ('Topics_Name', models.CharField(default=0, max_length=100, null=True, verbose_name='Konu Adı')),
                ('Question_Types', models.CharField(default=0, max_length=20, null=True, verbose_name='SORU TİPLERİ')),
                ('Level', models.CharField(blank=True, default=0, max_length=6)),
                ('Question_ID', models.CharField(blank=True, default=0, max_length=30)),
                ('Question_Image', models.ImageField(blank=True, null=True, upload_to='question_images/', verbose_name='Soruya Fotoğraf Ekleyin')),
                ('Created_Date', models.DateTimeField(auto_now=True, verbose_name='Oluşturma Tarihi')),
                ('author', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Soruyu Yazan')),
            ],
        ),
    ]