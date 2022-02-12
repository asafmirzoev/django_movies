# Generated by Django 3.2 on 2022-01-17 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(max_length=50, null=True, verbose_name='Трейлер'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='draft',
            field=models.BooleanField(default=False, verbose_name='Черновик'),
        ),
    ]