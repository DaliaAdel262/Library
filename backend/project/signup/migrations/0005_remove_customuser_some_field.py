# Generated by Django 5.0.6 on 2024-05-13 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0004_customuser_some_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='some_field',
        ),
    ]
