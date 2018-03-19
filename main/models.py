from django.db import models
from django.contrib.auth.models import User
from tags.models import Tag
from django.urls import reverse

class Article(models.Model):

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created'
    )
    image = models.ImageField(
        upload_to='articles_images',
        verbose_name="image"
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
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Author",
    )

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("main:single_art", args=[self.id])
