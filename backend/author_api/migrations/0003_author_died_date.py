# Generated by Django 5.1.1 on 2024-09-06 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_api', '0002_author_added_by_author_added_date_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='died_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
