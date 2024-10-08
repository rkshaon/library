# Generated by Django 5.1.1 on 2024-09-11 20:40

import BookShelf.utilities.storage
import book_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0011_alter_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, storage=BookShelf.utilities.storage.ReplaceExistingFileStorage(), upload_to=book_api.models.cover_upload_path),
        ),
    ]
