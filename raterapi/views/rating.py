from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game
from raterapi.models import Gamer
from raterapi.models import GameRating

class RatingView(ViewSet):
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
        

    # def list(self, request):
    #     review = Review.objects.all() 
    #     game = request.query_params.get('game', None)
    #     if game is not None:
    #         review = review.filter(game=game)
    #     serializer = ReviewSerializer(review, many=True)
    #     return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""
        gamer = Gamer.objects.get(user=request.auth.user)
        game = Game.objects.get(pk=request.data["game"])

        rating = GameRating.objects.create(
            game=game,
            gamer=gamer,
            rating=request.data["rating"]
        )
        serializer = RatingSerializer(rating)
        return Response(serializer.data)

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



class RatingSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = GameRating
        fields = ('id', 'game', 'gamer', 'rating')
        depth = 1