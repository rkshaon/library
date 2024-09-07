# Generated by Django 5.1.1 on 2024-09-07 13:43

import book_api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0007_book_topics'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_code',
            field=models.CharField(default=book_api.models.generate_book_code, editable=False, max_length=255, unique=True),
        ),
    ]
