from django.db import models

# Create your models here.
class PosterArt(models.Model):
    url=models.TextField(default="")
    width=models.FloatField(default=0)
    height=models.FloatField(default=0)
    
class ImageList(models.Model):
    posterArt=models.OneToOneField(
        PosterArt,
        null=True,
        on_delete=models.CASCADE
    )

class Movie(models.Model):
    title= models.CharField(max_length=200,unique=True)
    description= models.TextField()
    releaseYear= models.IntegerField(default=0)
    images=models.OneToOneField(ImageList,null=True,on_delete=models.CASCADE)
    
