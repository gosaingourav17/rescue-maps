# Generated by Django 2.1.2 on 2018-10-27 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0017_profile_bedsno'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='rescuelevel',
        ),
    ]