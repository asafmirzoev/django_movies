# Generated by Django 3.2 on 2022-01-18 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0013_alter_serial_poster'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Serial',
        ),
    ]