# Generated by Django 2.1.2 on 2018-10-28 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flood', '0019_userdata_degree'),
    ]

    operations = [
        migrations.CreateModel(
            name='rescueCenter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('lattitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
            ],
        ),
    ]