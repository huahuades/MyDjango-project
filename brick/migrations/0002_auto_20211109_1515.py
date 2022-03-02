# Generated by Django 3.2.9 on 2021-11-09 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brick', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brick',
            name='quantity',
            field=models.IntegerField(default='1000', max_length=50, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='brick',
            name='name',
            field=models.CharField(default='道牙石', max_length=50, verbose_name='石头名称'),
        ),
    ]
