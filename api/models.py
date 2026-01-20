from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Singer(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Song(models.Model):
    title = models.CharField(max_length=100)
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name='rt_song')

    def __str__(self):
        return self.title