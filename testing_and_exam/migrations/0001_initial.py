# Generated by Django 5.0.6 on 2024-05-15 12:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0003_alter_profile_followers_alter_profile_following'),
    ]

    operations = [
        migrations.CreateModel(
            name='AYT_Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=15, null=True, verbose_name='HANGİ SENENİN SORUSU ?')),
                ('Lessons_Name', models.CharField(choices=[('Matematik', 'Matematik'), ('Fizik', 'Fizik'), ('Kimya', 'Kimya'), ('Tarih', 'Tarih'), ('Biyoloji', 'Biyoloji'), ('Coğrafya', 'Coğrafya'), ('Din Kültürü ve Ahlak Bilgisi', 'Din Kültürü ve Ahlak Bilgisi')], max_length=100, verbose_name='DERS ADI')),
                ('EXAM_Name', models.TextField(choices=[('10 Haziran 2017', '10 Haziran 2017'), ('10 Haziran 2017', '23 Haziran 2018'), ('10 Haziran 2017', '15 Haziran 2019'), ('10 Haziran 2017', '27 Haziran 2020'), ('10 Haziran 2017', '26 Haziran 2021'), ('10 Haziran 2017', '18 Haziran 2022'), ('10 Haziran 2017', '17 Haziran 2023')], max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Question', models.TextField(verbose_name='SORU')),
                ('Choice_A', models.TextField(blank=True, null=True, verbose_name='A ŞIKKI')),
                ('Choice_B', models.TextField(blank=True, null=True, verbose_name='B ŞIKKI')),
                ('Choice_C', models.TextField(blank=True, null=True, verbose_name='C ŞIKKI')),
                ('Choice_D', models.TextField(blank=True, null=True, verbose_name='D ŞIKKI')),
                ('Choice_E', models.TextField(blank=True, null=True, verbose_name='E ŞIKKI')),
                ('Answer_Choice', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, verbose_name='CEVAP')),
                ('Question_Image', models.ImageField(blank=True, null=True, upload_to='testing_and_exam_images/', verbose_name='SORUYA FOTOĞRAF EKLEYİN')),
                ('Created_Date', models.DateTimeField(auto_now=True, verbose_name='OLUŞTURMA TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SORUYU YAZAN')),
            ],
        ),
        migrations.CreateModel(
            name='AYT_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.CharField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Question_Id', models.IntegerField(blank=True, null=True, verbose_name='SORU ID')),
                ('Question_Key', models.CharField(blank=True, max_length=1, null=True, verbose_name='SORUNUN CEVAP ANAHTARI')),
                ('author_Key', models.CharField(max_length=1, verbose_name='CEVAP VERİLEN ŞIK')),
                ('True_Answer', models.CharField(blank=True, default=2, max_length=1, null=True, verbose_name="CEVAP DOĞRU MU? ('0 => Yanlış, 1 => Doğru, 2 => Boş')")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='CEVAP VEREN')),
            ],
        ),
        migrations.CreateModel(
            name='AYT_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.CharField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Total_Number_Of_Questions', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM SORU SAYISI')),
                ('Number_Of_True', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM DOĞRU SAYISI')),
                ('Number_Of_False', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM YANLIŞ SAYISI')),
                ('Number_Of_Empty', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM BOŞ SAYISI')),
                ('Exam_Score', models.CharField(blank=True, max_length=3, null=True, verbose_name='SINAVDAN ALDIĞI PUAN')),
                ('Exam_Rating', models.CharField(blank=True, max_length=3, null=True, verbose_name='SINAV DERECESİ')),
                ('Completion_Time', models.CharField(blank=True, max_length=50, null=True, verbose_name='SINAV BİTİRME SÜRESİ')),
                ('Exam_Date', models.DateTimeField(verbose_name='SINAV BİTİRME TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SINAVA KATILAN')),
            ],
        ),
        migrations.CreateModel(
            name='AYT_TIMER_S',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.TextField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('hour_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='SAAT:')),
                ('minute_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='DAKİKA:')),
                ('Testing_Name_Exam_Date', models.DateTimeField(auto_now=True, verbose_name='SINAV SÜRESİ KAYIT TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SINAV SÜRESİNİ YAZAN KİŞİ')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Question_Id', models.IntegerField(blank=True, null=True, verbose_name='SORU ID')),
                ('Question_Key', models.CharField(blank=True, max_length=1, null=True, verbose_name='SORUNUN CEVAP ANAHTARI')),
                ('author_Key', models.CharField(max_length=1, verbose_name='CEVAP VERİLEN ŞIK')),
                ('True_Answer', models.CharField(blank=True, default=2, max_length=1, null=True, verbose_name="CEVAP DOĞRU MU? ('0 => Yanlış, 1 => Doğru, 2 => Boş')")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='CEVAP VEREN')),
            ],
        ),
        migrations.CreateModel(
            name='Exam_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Total_Number_Of_Questions', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM SORU SAYISI')),
                ('Number_Of_True', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM DOĞRU SAYISI')),
                ('Number_Of_False', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM YANLIŞ SAYISI')),
                ('Number_Of_Empty', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM BOŞ SAYISI')),
                ('Exam_Score', models.CharField(blank=True, max_length=3, null=True, verbose_name='SINAVDAN ALDIĞI PUAN')),
                ('Exam_Rating', models.CharField(blank=True, max_length=3, null=True, verbose_name='SINAV DERECESİ')),
                ('Completion_Time', models.CharField(blank=True, max_length=50, null=True, verbose_name='SINAV BİTİRME SÜRESİ')),
                ('Exam_Date', models.DateTimeField(verbose_name='SINAV BİTİRME TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SINAVA KATILAN')),
            ],
        ),
        migrations.CreateModel(
            name='Question_Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_Choice', models.CharField(choices=[('9. Sınıf', '9. Sınıf'), ('10. Sınıf', '10. Sınıf'), ('11. Sınıf', '11. Sınıf'), ('12. Sınıf', '12. Sınıf')], max_length=15, null=True, verbose_name='KAIÇINCI SINIF SORUSU ?')),
                ('Lessons_Name', models.CharField(choices=[('Türk Dili ve Edebiyatı', 'Türk Dili ve Edebiyatı'), ('Matematik', 'Matematik'), ('Fizik', 'Fizik'), ('Kimya', 'Kimya'), ('Tarih', 'Tarih'), ('Biyoloji', 'Biyoloji'), ('Coğrafya', 'Coğrafya'), ('Din Kültürü ve Ahlak Bilgisi', 'Din Kültürü ve Ahlak Bilgisi')], max_length=100, verbose_name='DERS ADI')),
                ('Period_Name', models.CharField(choices=[('1. Dönem', '1. Dönem'), ('2. Dönem', '2. Dönem')], max_length=13, verbose_name='DÖNEM ADI ?')),
                ('Exam_Name', models.TextField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Question', models.TextField(verbose_name='SORU')),
                ('Choice_A', models.TextField(blank=True, null=True, verbose_name='A ŞIKKI')),
                ('Choice_B', models.TextField(blank=True, null=True, verbose_name='B ŞIKKI')),
                ('Choice_C', models.TextField(blank=True, null=True, verbose_name='C ŞIKKI')),
                ('Choice_D', models.TextField(blank=True, null=True, verbose_name='D ŞIKKI')),
                ('Choice_E', models.TextField(blank=True, null=True, verbose_name='E ŞIKKI')),
                ('Answer_Choice', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, verbose_name='CEVAP')),
                ('Question_Image', models.ImageField(blank=True, null=True, upload_to='testing_and_exam_images/', verbose_name='SORUYA FOTOĞRAF EKLEYİN')),
                ('Created_Date', models.DateTimeField(auto_now=True, verbose_name='OLUŞTURMA TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SORUYU YAZAN')),
            ],
        ),
        migrations.CreateModel(
            name='Testing_Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Class_Choice', models.CharField(choices=[('9. Sınıf', '9. Sınıf'), ('10. Sınıf', '10. Sınıf'), ('11. Sınıf', '11. Sınıf'), ('12. Sınıf', '12. Sınıf')], max_length=15, null=True, verbose_name='KAIÇINCI SINIF SORUSU ?')),
                ('Lessons_Name', models.CharField(choices=[('Türk Dili ve Edebiyatı', 'Türk Dili ve Edebiyatı'), ('Matematik', 'Matematik'), ('Fizik', 'Fizik'), ('Kimya', 'Kimya'), ('Tarih', 'Tarih'), ('Biyoloji', 'Biyoloji'), ('Coğrafya', 'Coğrafya'), ('Din Kültürü ve Ahlak Bilgisi', 'Din Kültürü ve Ahlak Bilgisi')], max_length=100, verbose_name='DERS ADI')),
                ('Testing_Name', models.TextField(blank=True, max_length=100, null=True, verbose_name='TEST ADI')),
                ('Question', models.TextField(verbose_name='SORU')),
                ('Choice_A', models.TextField(blank=True, null=True, verbose_name='A ŞIKKI')),
                ('Choice_B', models.TextField(blank=True, null=True, verbose_name='B ŞIKKI')),
                ('Choice_C', models.TextField(blank=True, null=True, verbose_name='C ŞIKKI')),
                ('Choice_D', models.TextField(blank=True, null=True, verbose_name='D ŞIKKI')),
                ('Choice_E', models.TextField(blank=True, null=True, verbose_name='E ŞIKKI')),
                ('Answer_Choice', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, verbose_name='CEVAP')),
                ('Question_Image', models.ImageField(blank=True, null=True, upload_to='testing_and_exam_images/', verbose_name='SORUYA FOTOĞRAF EKLEYİN')),
                ('Created_Date', models.DateTimeField(auto_now=True, verbose_name='OLUŞTURMA TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SORUYU YAZAN')),
            ],
        ),
        migrations.CreateModel(
            name='Testing_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Testing_Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='DENEME ADI')),
                ('Question_Id', models.IntegerField(blank=True, null=True, verbose_name='SORU ID')),
                ('Question_Key', models.CharField(blank=True, max_length=1, null=True, verbose_name='SORUNUN CEVAP ANAHTARI')),
                ('author_Key', models.CharField(max_length=1, verbose_name='CEVAP VERİLEN ŞIK')),
                ('True_Answer', models.CharField(blank=True, default=2, max_length=1, null=True, verbose_name="CEVAP DOĞRU MU? ('0 => Yanlış, 1 => Doğru, 2 => Boş')")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='CEVAP VEREN')),
            ],
        ),
        migrations.CreateModel(
            name='Testing_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Testing_Name', models.CharField(blank=True, max_length=100, null=True, verbose_name='DENEME ADI')),
                ('Total_Number_Of_Questions', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM SORU SAYISI')),
                ('Number_Of_True', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM DOĞRU SAYISI')),
                ('Number_Of_False', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM YANLIŞ SAYISI')),
                ('Number_Of_Empty', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM BOŞ SAYISI')),
                ('Testing_Score', models.CharField(blank=True, max_length=3, null=True, verbose_name='DENEMEDEN ALDIĞI PUAN')),
                ('Testing_Rating', models.CharField(blank=True, max_length=3, null=True, verbose_name='DENEME DERECESİ')),
                ('Completion_Time', models.CharField(blank=True, max_length=50, null=True, verbose_name='DENEME BİTİRME SÜRESİ')),
                ('Testing_Date', models.DateTimeField(verbose_name='DENEME BİTİRME TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='DENEMEMEYE KATILAN')),
            ],
        ),
        migrations.CreateModel(
            name='TIMER_S',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exam_Name', models.TextField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('hour_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='SAAT:')),
                ('minute_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='DAKİKA:')),
                ('TIMER_S_Exam_Date', models.DateTimeField(auto_now=True, verbose_name='SINAV SÜRESİ KAYIT TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SINAV SÜRESİNİ YAZAN KİŞİ')),
            ],
        ),
        migrations.CreateModel(
            name='TIMER_S_TESTTING',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Testing_Name', models.TextField(blank=True, max_length=100, null=True, verbose_name='TEST ADI')),
                ('hour_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='SAAT:')),
                ('minute_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='DAKİKA:')),
                ('Testing_Name_Exam_Date', models.DateTimeField(auto_now=True, verbose_name='TEST SÜRESİ KAYIT TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='TEST SÜRESİNİ YAZAN KİŞİ')),
            ],
        ),
        migrations.CreateModel(
            name='TIMER_S_TYT',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.TextField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('hour_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='SAAT:')),
                ('minute_s', models.PositiveSmallIntegerField(blank=True, default=0, null=True, verbose_name='DAKİKA:')),
                ('Testing_Name_Exam_Date', models.DateTimeField(auto_now=True, verbose_name='SINAV SÜRESİ KAYIT TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SINAV SÜRESİNİ YAZAN KİŞİ')),
            ],
        ),
        migrations.CreateModel(
            name='TYT_Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.CharField(choices=[('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023')], max_length=15, null=True, verbose_name='HANGİ SENENİN SORUSU ?')),
                ('Lessons_Name', models.CharField(choices=[('Matematik', 'Matematik'), ('Fizik', 'Fizik'), ('Kimya', 'Kimya'), ('Tarih', 'Tarih'), ('Biyoloji', 'Biyoloji'), ('Coğrafya', 'Coğrafya'), ('Din Kültürü ve Ahlak Bilgisi', 'Din Kültürü ve Ahlak Bilgisi')], max_length=100, verbose_name='DERS ADI')),
                ('EXAM_Name', models.TextField(choices=[('10 Haziran 2017', '10 Haziran 2017'), ('10 Haziran 2017', '23 Haziran 2018'), ('10 Haziran 2017', '15 Haziran 2019'), ('10 Haziran 2017', '27 Haziran 2020'), ('10 Haziran 2017', '26 Haziran 2021'), ('10 Haziran 2017', '18 Haziran 2022'), ('10 Haziran 2017', '17 Haziran 2023')], max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Question', models.TextField(verbose_name='SORU')),
                ('Choice_A', models.TextField(blank=True, null=True, verbose_name='A ŞIKKI')),
                ('Choice_B', models.TextField(blank=True, null=True, verbose_name='B ŞIKKI')),
                ('Choice_C', models.TextField(blank=True, null=True, verbose_name='C ŞIKKI')),
                ('Choice_D', models.TextField(blank=True, null=True, verbose_name='D ŞIKKI')),
                ('Choice_E', models.TextField(blank=True, null=True, verbose_name='E ŞIKKI')),
                ('Answer_Choice', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1, verbose_name='CEVAP')),
                ('Question_Image', models.ImageField(blank=True, null=True, upload_to='testing_and_exam_images/', verbose_name='SORUYA FOTOĞRAF EKLEYİN')),
                ('Created_Date', models.DateTimeField(auto_now=True, verbose_name='OLUŞTURMA TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SORUYU YAZAN')),
            ],
        ),
        migrations.CreateModel(
            name='TYT_Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.CharField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Question_Id', models.IntegerField(blank=True, null=True, verbose_name='SORU ID')),
                ('Question_Key', models.CharField(blank=True, max_length=1, null=True, verbose_name='SORUNUN CEVAP ANAHTARI')),
                ('author_Key', models.CharField(max_length=1, verbose_name='CEVAP VERİLEN ŞIK')),
                ('True_Answer', models.CharField(blank=True, default=2, max_length=1, null=True, verbose_name="CEVAP DOĞRU MU? ('0 => Yanlış, 1 => Doğru, 2 => Boş')")),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='CEVAP VEREN')),
            ],
        ),
        migrations.CreateModel(
            name='TYT_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date_Choice', models.CharField(blank=True, max_length=100, null=True, verbose_name='SINAV ADI')),
                ('Total_Number_Of_Questions', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM SORU SAYISI')),
                ('Number_Of_True', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM DOĞRU SAYISI')),
                ('Number_Of_False', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM YANLIŞ SAYISI')),
                ('Number_Of_Empty', models.CharField(blank=True, max_length=3, null=True, verbose_name='TOPLAM BOŞ SAYISI')),
                ('Exam_Score', models.CharField(blank=True, max_length=3, null=True, verbose_name='SINAVDAN ALDIĞI PUAN')),
                ('Exam_Rating', models.CharField(blank=True, max_length=3, null=True, verbose_name='SINAV DERECESİ')),
                ('Completion_Time', models.CharField(blank=True, max_length=50, null=True, verbose_name='SINAV BİTİRME SÜRESİ')),
                ('Exam_Date', models.DateTimeField(verbose_name='SINAV BİTİRME TARİHİ')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SINAVA KATILAN')),
            ],
        ),
    ]