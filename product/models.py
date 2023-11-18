from django.db import models

from category.models import Category
from django.utils.text import slugify


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    img = models.ImageField(upload_to='media/products/')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name='product')
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            # models.Index(fields=['-created'])
        ]
        
    def __str__(self) -> str:
        return self.title
    
