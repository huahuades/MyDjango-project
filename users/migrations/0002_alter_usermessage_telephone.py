# Generated by Django 3.2.9 on 2021-11-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermessage',
            name='telephone',
            field=models.IntegerField(null=True, verbose_name='用户电话号码'),
        ),
    ]
