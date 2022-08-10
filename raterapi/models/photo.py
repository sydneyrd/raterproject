from django.db import models

class Photo(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.DO_NOTHING, related_name='pictures')
    photo = models.ImageField(
        upload_to='actionimages', height_field=None,
        width_field=None, max_length=None, null=True)

