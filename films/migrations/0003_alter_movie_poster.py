# Generated by Django 3.2 on 2022-01-17 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_auto_20220117_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(upload_to='movies/<django.db.models.fields.CharField>', verbose_name='Постер'),
        ),
    ]
