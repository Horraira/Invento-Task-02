from rest_framework import generics
from .serializers import LinkSerializer, UrlShorten
from main.models import LinkMapping
from rest_framework.permissions import IsAuthenticated


class getData(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = LinkMapping.objects.all()
    serializer_class = LinkSerializer


class shortenUrl(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = LinkMapping.objects.all()
    serializer_class = UrlShorten
