# Generated by Django 4.2.3 on 2023-08-19 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mangas',
            old_name='book_description',
            new_name='manga_description',
        ),
        migrations.RenameField(
            model_name='mangas',
            old_name='book_pdf',
            new_name='manga_pdf',
        ),
        migrations.RenameField(
            model_name='mangas',
            old_name='book_photo',
            new_name='manga_photo',
        ),
    ]