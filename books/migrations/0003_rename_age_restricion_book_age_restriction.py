# Generated by Django 4.1.7 on 2023-03-11 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_genre_alter_book_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='age_restricion',
            new_name='age_restriction',
        ),
    ]