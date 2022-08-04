# coding=utf-8

from django.db import models
from django.urls import reverse


class Book(models.Model):
    name = models.CharField(u'Название', max_length=64)
    author = models.CharField(u'Автор', max_length=64)
    pub_date = models.DateField(u'Дата публикации')
    slug = models.SlugField(max_length=50, default='')

    def __str__(self):
        return self.name + " " + self.author

