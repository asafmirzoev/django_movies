# Generated by Django 3.2 on 2022-01-18 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0010_auto_20220119_0009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movies/<django.db.models.fields.CharField>/', verbose_name='Постер'),
        ),
        migrations.AlterField(
            model_name='serial',
            name='poster',
            field=models.ImageField(upload_to='serials/<django.db.models.fields.CharField>/', verbose_name='Постер'),
        ),
    ]
