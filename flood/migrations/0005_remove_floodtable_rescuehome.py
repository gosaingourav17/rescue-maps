# Generated by Django 2.1.2 on 2018-10-13 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0004_auto_20181013_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='floodtable',
            name='rescueHome',
        ),
    ]