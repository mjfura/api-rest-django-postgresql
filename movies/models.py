from django.db import models

# Create your models here.
class PosterArt(models.Model):
    url=models.URLField(),
    width=models.FloatField(),
    height=models.FloatField(),
    
class ImageList(models.Model):
    posterArt=models.ManyToManyField(PosterArt)

class Movie(models.Model):
    title= models.CharField(max_length=200,unique=True)
    description= models.TextField()
    releaseYear= models.IntegerField(),
    images=models.ManyToManyField(ImageList)
    
