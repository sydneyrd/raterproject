from django.db import models

class Photo(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    photo = models.CharField(max_length=250)