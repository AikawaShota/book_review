# Generated by Django 4.1.2 on 2022-11-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_alter_book_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='poster',
            field=models.CharField(default='admin', max_length=50),
            preserve_default=False,
        ),
    ]
