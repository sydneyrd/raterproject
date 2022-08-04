from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from raterapi.views.game import GameView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from raterapi.views import register_user, login_user, GameView

#
# router.register(r'gametypes', GameTypeView, 'gametype')
# router.register(r'events', EventView, 'event')
# router.register(r'games', GameView, 'games' )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'games')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    
]
