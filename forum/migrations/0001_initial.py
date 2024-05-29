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
            name='FORUM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True, verbose_name='Forum Metin')),
                ('topic_type', models.CharField(choices=[('Genel', 'Genel'), ('Tartışma', 'Tartışma'), ('Soru-Cevap', 'Soru-Cevap')], max_length=50, null=True, verbose_name='Konu Türü(Tipi)')),
                ('number_of_answers', models.CharField(default='0', max_length=50, null=True, verbose_name='Cevap Sayısı')),
                ('last_reply_date', models.CharField(default='0', max_length=50, verbose_name='Son Cevap Tarihi')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturma Tarihi')),
                ('forum_image', models.ImageField(blank=True, null=True, upload_to='forum/', verbose_name='Foruma Fotoğraf Ekleyin')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='ENTRY YAZAN KİŞİ')),
            ],
        ),
        migrations.CreateModel(
            name='Forum_Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forum_text_id', models.IntegerField(verbose_name='Yorum Yapılan Metin ID')),
                ('comment_content', models.TextField(null=True, verbose_name='Yorum')),
                ('created_date', models.DateTimeField(auto_now=True, verbose_name='Oluşturma Tarihi')),
                ('comment_author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='user.profile', verbose_name='YORUM YAPAN')),
            ],
        ),
        migrations.CreateModel(
            name='Forum_Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.profile', verbose_name='SORUYU BEĞENEN')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to='forum.forum', verbose_name='BEĞENİ YAPILAN FORUM')),
            ],
            options={
                'unique_together': {('author', 'forum')},
            },
        ),
    ]
