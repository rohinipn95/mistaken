from django.db import models

# Create your models here.
class meet_team(models.Model):
    name = models.CharField(max_length=256)
    photo=models.ImageField(upload_to='pic')
    about=models.TextField()

    def __str__(self):
        return self.name
class Place(models.Model):
    name=models.CharField(max_length=256)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

