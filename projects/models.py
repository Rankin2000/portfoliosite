from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.name}"

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='uploads/', blank=True)
    date = models.DateField()

    URLINTRO_CHOICES = (
        ('repo', "The repo for this can be found "),
        ('video', "The video for this can be found "),
        ('link', "The link for this can be found "),
        )


    urlintro = models.CharField(
            max_length=100,
            choices = URLINTRO_CHOICES,
            blank=True
            )
    url = models.URLField(blank=True)
    categories = models.ManyToManyField('Category', related_name='projects')
    class Meta:
        ordering = ['-date']


    def __str__(self):
        return f"{self.title}"
