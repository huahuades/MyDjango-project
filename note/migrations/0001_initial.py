# Generated by Django 3.2.9 on 2021-11-17 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0005_alter_usermessage_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('content', models.TextField(verbose_name='内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('usermessage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.usermessage')),
            ],
            options={
                'verbose_name': '意见反馈',
                'verbose_name_plural': '意见反馈',
                'db_table': 'note',
            },
        ),
    ]
