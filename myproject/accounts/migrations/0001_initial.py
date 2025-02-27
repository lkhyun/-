# Generated by Django 4.1 on 2022-08-19 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=20, unique=True, verbose_name='유저 아이디')),
                ('user_pw', models.CharField(max_length=30, verbose_name='비밀번호')),
                ('user_name', models.CharField(max_length=15, unique=True, verbose_name='이름')),
                ('user_email', models.EmailField(max_length=100, unique=True, verbose_name='이메일')),
                ('user_register_dttm', models.DateTimeField(auto_now_add=True, verbose_name='계정생성시간')),
            ],
        ),
    ]
