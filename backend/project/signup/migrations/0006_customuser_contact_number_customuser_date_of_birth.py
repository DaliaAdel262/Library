# Generated by Django 5.0.6 on 2024-05-21 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0005_remove_customuser_some_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='contact_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
