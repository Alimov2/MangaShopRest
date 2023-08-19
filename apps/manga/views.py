from rest_framework import generics, viewsets
from apps.manga.models import Category, Mangas
from apps.manga.serializers import CategorySerializer, MangasSerializer

# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class MangasViewSet(viewsets.ModelViewSet):
    queryset = Mangas.objects.all()
    serializer_class = MangasSerializer