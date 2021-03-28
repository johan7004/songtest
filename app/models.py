from django.db import models


# Create your models here.

class Songs(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(null="false", unique=True)
    lyrics = models.TextField(verbose_name="lyrics")
    
    
    def __str__(self):
        return self.title
