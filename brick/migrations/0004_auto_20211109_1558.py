# Generated by Django 3.2.9 on 2021-11-09 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brick', '0003_alter_brick_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brick',
            name='quantity',
            field=models.IntegerField(verbose_name='数量'),
        ),
        migrations.AlterModelTable(
            name='brick',
            table='brick',
        ),
    ]
