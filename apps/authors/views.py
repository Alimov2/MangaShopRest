from rest_framework import generics, viewsets
from apps.authors.models import Authors
from apps.authors.serializers import AuthorsSerializer

class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer