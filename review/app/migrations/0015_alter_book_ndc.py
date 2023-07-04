# Generated by Django 4.1.2 on 2022-11-02 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_book_writer_alter_book_genre_alter_book_rating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ndc',
            field=models.CharField(blank=True, choices=[('総記', '総記'), ('哲学', '哲学'), ('歴史', '歴史'), ('社会科学', '社会科学'), ('自然科学', '自然科学'), ('技術. 工学', '技術. 工学'), ('産業', '産業'), ('芸術. 美術', '芸術. 美術'), ('言語', '言語'), ('文学', '文学'), ('不明', '不明')], max_length=6, null=True, verbose_name='NDC'),
        ),
    ]
