from django.utils.text import slugify # < here
from django.db import models
from django.urls import reverse # < here
class Flower(models.Model):
    title = models.CharField(max_length=255, default='')
    description = models.TextField(default='')
    slug = models.SlugField(blank=True, default='') # < here
def __str__(self):
    return self.title
def save(self, *args, **kwargs): # < here
    self.slug = slugify(self.title)
    super(Flower, self).save()
def get_absolute_url(self): # < here
    #return reverse('detail', args=[str(self.slug)])
    #return reverse('detail', kwargs={'slug': self.slug})
    return self.slug