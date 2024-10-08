from django.db import models
from djrichtextfield.models import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.name}"

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    def __str__(self):
        return f"{self.title}"
