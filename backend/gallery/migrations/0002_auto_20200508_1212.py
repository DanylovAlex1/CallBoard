# Generated by Django 3.0.6 on 2020-05-08 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='photo',
            new_name='photos',
        ),
    ]
