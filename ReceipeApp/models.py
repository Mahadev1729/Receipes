from django.db import models #type:ignore

# Create your models here.
class Receipe(models.Model):
    receipe_name=models.CharField(max_length=100);
    receipe_disc=models.TextField()
    receipe_image=models.ImageField()
    
    
