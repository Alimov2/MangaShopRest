from rest_framework import generics, viewsets, mixins
from apps.users.models import User
from apps.users.serializers import UserSerializer, RegisterSerializer
# Create your views here.
    
    
class RegisterAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
    
class UserViewSet(mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer