from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from raterapi.models import Game
from raterapi.models import Gamer
from django.db.models import Q

class GameView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type
        Returns:
            Response -- JSON serialized game type"""
        try:
            game = Game.objects.get(pk=pk)
            serializer = GameSerializer(game)
            return Response(serializer.data)
        except Game.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        

    def list(self, request):
        """Handle GET requests to get all game types
        Returns:
            Response -- JSON serialized list of game types
        """
        games = Game.objects.all()
        search_text = self.request.query_params.get('q', None)
        if search_text is not None:
            games = Game.objects.filter(
                    Q(title__contains=search_text) |
                    Q(description__contains=search_text) |
                    Q(designer__contains=search_text))
        order = self.request.query_params.get('orderby', None)
        if order is not None:
                games = Game.objects.order_by(order)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations"""

        game = Game.objects.create(
            title=request.data["title"],
            designer=request.data["designer"],
            number_of_players=request.data["number_of_players"],
            time=request.data["time"],
            release_date=request.data["release_date"],
            age_rating=request.data["age_rating"],
            description=request.data["description"]
        )
        serializer = GameSerializer(game)
        return Response(serializer.data)

    def update(self, request, pk):
        """handle put"""
        game = Game.objects.get(pk=pk)
        game.title = request.data["title"]
        game.designer = request.data["designer"]
        game.number_of_players = request.data["number_of_players"]
        game.time = request.data["time"]
        game.release_date = request.data["release_date"]
        game.age_rating = request.data["age_rating"]
        game.description = request.data["description"]
        game.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

    # def destroy(self, request, pk):
    #     game = Game.objects.get(pk=pk)
    #     game.delete()
    #     return Response(None, status=status.HTTP_204_NO_CONTENT)



class GameSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Game
        fields = ('id', 'title', 'description', 'designer', 'release_date', 'number_of_players',  'time', 'age_rating', 'average_rating', 'categories')
        depth = 2