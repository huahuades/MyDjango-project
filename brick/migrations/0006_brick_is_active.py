# Generated by Django 3.2.9 on 2021-11-12 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brick', '0005_brick_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='brick',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活跃'),
        ),
    ]
