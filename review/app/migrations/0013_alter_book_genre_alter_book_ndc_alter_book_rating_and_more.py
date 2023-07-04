# Generated by Django 4.1.2 on 2022-11-02 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_book_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Genre'),
        ),
        migrations.AlterField(
            model_name='book',
            name='ndc',
            field=models.CharField(choices=[('総記', '総記'), ('哲学', '哲学'), ('歴史', '歴史'), ('社会科学', '社会科学'), ('自然科学', '自然科学'), ('技術. 工学', '技術. 工学'), ('産業', '産業'), ('芸術. 美術', '芸術. 美術'), ('言語', '言語'), ('文学', '文学'), ('不明', '不明')], max_length=6, verbose_name='NDC'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], default=1, max_length=1, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
    ]
