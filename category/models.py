from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255,)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='media/category_images', verbose_name='Фото категории', null=True)
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


    def __str__(self) -> str:
        return self.title
