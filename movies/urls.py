from rest_framework import routers
from movies.views import MovieViewSet
from movies.views import ImageListViewSet
from movies.views import PosterArtViewSet
# import views
#from movies import views
#urlpatterns = [
#    path("movies/",views.Movies.as_view())
#]
router=routers.DefaultRouter()
router.register("movies",MovieViewSet,"movies")
router.register("image-list",ImageListViewSet,"image-list")
router.register("poster-art",PosterArtViewSet,"poster-art")
urlpatterns=router.urls