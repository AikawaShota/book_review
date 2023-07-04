from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=50)
    writer = models.CharField(max_length=50, null=True)
    ndc_tuple = ('総記', '総記'), ('哲学', '哲学'), ('歴史', '歴史'), ('社会科学', '社会科学'),('自然科学', '自然科学'),('技術. 工学', '技術. 工学'), ('産業', '産業'), ('芸術. 美術', '芸術. 美術'),('言語', '言語'), ('文学', '文学'), ('不明', '不明')
    ndc = models.CharField(verbose_name='NDC', max_length=6, choices=ndc_tuple)
    tag = models.CharField(max_length=20, null=True, blank=True)
    summary = models.TextField(max_length=500, null=True)
    review = models.TextField(max_length=500, null=True)
    rating_tuple = ('0', '0'), ('0.5', '0.5'), ('1', '1'), ('1.5', '1.5'), ('2', '2'), ('2.5', '2.5'), ('3', '3'), ('3.5', '3.5'), ('4', '4'), ('4.5', '4.5'), ('5', '5')
    rating = models.CharField(max_length=3, choices=rating_tuple)
    poster = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'BookReview'
        db_table = 'review_table'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'pk':self.pk})
