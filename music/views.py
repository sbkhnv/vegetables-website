from django.db.transaction import atomic
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artist,Albom,Songs
from .serializers import ArtistSerializer,AlbomSerializer,SongsSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter
from rest_framework import filters, status
from rest_framework.pagination import LimitOffsetPagination
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
    # permission_classes = (IsAuthenticated, )

    @action(detail=False,methods=['POST'])
    def artist(self,request,*args,**kwargs):
        albom = self.get_object()
        albom = albom.albom.artist
        serializer = ArtistSerializer(albom)
        return Response(data=serializer.data)

    @action(detail=True, methods=["GET"])
    def popular(self, request, *args, **kwargs):
        albom = self.get_object()
        with atomic():
            albom.popular += 1
            albom.save()
            return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['GET'])
    def top_albom(self, request, *args, **kwargs):
        albom = self.get_queryset()
        albom = albom.order_by('-popular')[:1]
        serializer = SongsSerializer(albom, many=True)
        return Response(data=serializer.data)


# class SongsAPIView(APIView):
#     def get(self,request):
#         songs = Songs.objects.all()
#         serializer = SongsSerializer(songs)
#         return Response(data=serializer.data)


class SongSetApiView(ModelViewSet):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer
    # authentication_classes = (TokenAuthentication, )
    # permission_classes = (IsAuthenticated, )
    filter_backends = (filters.SearchFilter, )
    search_fields = ['title', ]  # ['^title', ] ['@title', ] ['=title', ]
    pagination_class = LimitOffsetPagination

    @action(detail=True, methods=["GET"])
    def listen(self,request,*args,**kwargs):
        song = self.get_object()
        with atomic():
            song.listened += 1
            song.save()
            return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=False,methods=['GET'])
    def top(self,request,*args,**kwargs):
        songs = self.get_queryset()
        songs = songs.order_by('-listened')[:3]
        serializer = SongsSerializer(songs,many=True)
        return Response(data=serializer.data)


    @action(detail=False,methods=['POST'])
    def albom(self,request,*args,**kwargs):
        songs = self.get_object()
        albom = songs.albom
        serializer = AlbomSerializer(albom)
        return Response(data=serializer.data)



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
