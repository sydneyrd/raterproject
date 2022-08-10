import uuid
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game
from raterapi.models import Gamer
from raterapi.models import Photo
from django.core.files.base import ContentFile
import base64







class PhotoView(ViewSet):
    """Level up game types view"""

    # def retrieve(self, request, pk):
    #     """Handle GET requests for single game type
    #     Returns:
    #         Response -- JSON serialized game type"""
    #     try:
    #         review = Review.objects.get(pk=pk)
    #         serializer = ReviewSerializer(review)
    #         return Response(serializer.data)
    #     except Review.DoesNotExist as ex:
    #         return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        photo = Photo.objects.all() 
        game = request.query_params.get('game', None)
        if game is not None:
            photo = Photo.objects.filter(game=game)
        serializer = PhotoSerializer(photo, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])
        format, imgstr = request.data["photo"].split(';base64,')
        ext = format.split('/')[-1]
        data = ContentFile(base64.b64decode(imgstr), name=f'{request.data["game"]}-{uuid.uuid4()}.{ext}')
        pic = Photo.objects.create(
            game=game,
            gamer=gamer,
            photo=data
        )
        pic.save()
        serializer = PhotoSerializer(pic)
        return Response(serializer.data)




# Create a new instance of the game picture model you defined
# Example: game_picture = GamePicture()

# Give the image property of your game picture instance a value
# For example, if you named your property `action_pic`, then
# you would specify the following code:
#
#       game_picture.action_pic = data

# Save the data to the database with the save() method















    # def update(self, request, pk):
    #     """handle put"""
    #     game = Game.objects.get(pk=pk)
    #     game.title = request.data["title"]
    #     game.maker = request.data["maker"]
    #     game.number_of_players = request.data["number_of_players"]
    #     game.skill_level = request.data["skill_level"]

    #     game_type = GameType.objects.get(pk=request.data["game_type"])
    #     game.game_type = game_type
    #     game.save()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk):
    #     game = Game.objects.get(pk=pk)
    #     game.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)



class PhotoSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Photo
        fields = ('id', 'game', 'gamer', 'photo')
        depth = 1