# Generated by Django 4.1.2 on 2022-11-10 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_alter_book_rating_alter_book_summary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.TextField(max_length=500, null=True),
        ),
    ]
