# Generated by Django 5.1.1 on 2024-09-06 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_api', '0005_genre_book_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]
