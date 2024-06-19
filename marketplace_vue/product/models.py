from django.db import models
from io import BytesIO
from PIL import Image
from django.core.files import File


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f'/{self.slug}/'