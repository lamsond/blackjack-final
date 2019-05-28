from django.db import models

class Game(models.Model):
    player = models.CharField(max_length=3)
    wins = models.IntegerField()
    losses = models.IntegerField()

