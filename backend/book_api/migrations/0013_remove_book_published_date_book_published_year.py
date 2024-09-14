# Generated by Django 5.1.1 on 2024-09-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0012_alter_book_cover_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AddField(
            model_name='book',
            name='published_year',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
