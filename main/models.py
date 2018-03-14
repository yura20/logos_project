from django.db import models

from tags.models import Tag


class Article(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Title'
    )
    content = models.TextField(
        verbose_name='Content'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tags',
        help_text='Tags for dividing articles to categories',
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
