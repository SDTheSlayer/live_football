from django.db import models

class scores(models.Model):
    team1 =  models.CharField( max_length= 255)
    team2 = models.CharField(max_length=255)
    score1 = models.CharField(max_length=10)
    score2 = models.CharField(max_length=10)
    def __str__(self):
        return self.team1
# Create your models here.
