# Generated by Django 3.0.6 on 2020-05-08 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_auto_20200508_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='user',
        ),
    ]
