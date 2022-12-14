from rest_framework import viewsets,permissions,filters
from movies import serializers
from movies import models
# Create your views here.
#class Movies(APIView):
 #   def get(self,request,format=None):
  #      return Response({
   #         "message":"Testing Api Movies"
    #    })
class MovieViewSet(viewsets.ModelViewSet):
    queryset=models.Movie.objects.all().order_by("-releaseYear")
    permissions_classes=[permissions.AllowAny]
    serializer_class=serializers.MovieSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=["title"]

class PosterArtViewSet(viewsets.ModelViewSet):
    queryset=models.PosterArt.objects.all()
    permissions_classes=[permissions.AllowAny]
    serializer_class=serializers.PosterArtSerializer
    
class ImageListViewSet(viewsets.ModelViewSet):
    queryset=models.ImageList.objects.all()
    permissions_classes=[permissions.AllowAny]
    serializer_class=serializers.ImageListSerializer