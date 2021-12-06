from django.db import models
from django.urls import reverse

from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel
from stdimage import StdImageField


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(unique=True, populate_from='name', always_update=False)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book:list_by_category', kwargs={'slug': self.slug})


class Book(TimeStampedModel):
    title = models.CharField(max_length=150, verbose_name='Título do livro', help_text='Digite o título completo do livro.')
    slug = AutoSlugField(unique=True, populate_from='title', always_update=False)
    description = models.TextField(blank=True)
    cover = StdImageField(upload_to='cover_imgs/', blank=True, verbose_name='Imagem de capa', help_text='Faça upload da imagem de capa')
    is_published = models.BooleanField(default=False)
    category = models.ManyToManyField(Category, related_name='books', blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:detail', kwargs={'slug': self.slug})
