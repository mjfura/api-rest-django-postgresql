from rest_framework.views import APIView
from rest_framework.response import Response
from movies import models
# Create your views here.
class Movies(APIView):
    def get(self,request,format=None):
        return Response({
            "message":"Testing Api Movies"
        })