from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from raterapi.views.category import CategoryView
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from django.conf.urls.static import static
from django.conf import settings
from raterapi.views import register_user, login_user, GameView, GameCategoryView, ReviewView, RatingView, PhotoView

#
# router.register(r'gametypes', GameTypeView, 'gametype')
# router.register(r'events', EventView, 'event')
# router.register(r'games', GameView, 'games' )

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'games', GameView, 'games')
router.register(r'categories', CategoryView, 'categories')
router.register(r'gamecategories', GameCategoryView, 'gamecategories')
router.register(r'reviews', ReviewView, 'reviews')
router.register(r'ratings', RatingView, 'ratings')
router.register(r'photos', PhotoView, 'photo')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
