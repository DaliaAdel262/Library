# Generated by Django 5.0.6 on 2024-05-23 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_books', '0002_book_available'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
