from django.db import models

class GameCategories(models.Model):

    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)