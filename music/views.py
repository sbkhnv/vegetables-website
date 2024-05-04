from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artist,Albom,Songs
from .serializers import ArtistSerializer,AlbomSerializer,SongsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
class LandingPageAPIView(APIView):
    def get(self,request):
        return Response(data={"get": "yaxshi" })

    def post(self,request):
        return Response(data={"post": "yaxshi" })


class ArtistAPIView(APIView):
    def get(self,request):
        artist = Artist.objects.all()
        serializer = ArtistSerializer(artist,many=True)
        return Response(data=serializer.data)


#class AlbomAPIView(APIView):
#   def get(self,request):
#        albom = Albom.objects.all()
#        serializer = AlbomSerializer(Albom,many=True)
#        return Response(data=serializer.data)


class AlbomDetailApiView(ModelViewSet):
    queryset = Albom.objects.all()
    serializer_class = AlbomSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )


# class SongsAPIView(APIView):
#     def get(self,request):
#         songs = Songs.objects.all()
#         serializer = SongsSerializer(songs)
#         return Response(data=serializer.data)


class SongSetApiView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    # permission_classes = (AllowAny, )
    # def get(self,request,id):
    #     songs = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(songs)
    #     return Response(data=serializer.data)
    #
    # def post(self,request,id):
    #     song = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(song,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def put(self, request, id,format=None):
    #     obj = Songs.objects.get(id=id)
    #     serializer = SongsSerializer(obj,data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
    #
    #
    # def patch(self, request, pk,format=None):
    #     obj = Songs.objects.get(pk=pk)
    #     serializer = SongsSerializer(obj,data=request.data,partial=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         {
    #             'error': 'error',
    #             "message": "invalid data"
    #         }
    #     )
