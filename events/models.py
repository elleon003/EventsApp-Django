from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('events:events_list_by_category', args=[self.slug])


class Event(models.Model):
    category = models.ForeignKey(Category, related_name='events', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='events/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('events:event_detail', args=[self.id, self.slug])
    