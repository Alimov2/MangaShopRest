from rest_framework import serializers
from django.core.mail import send_mail
from django.contrib.auth.password_validation import validate_password
from apps.users.models import User
from apps.manga.serializers import MangasSerializer

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True,required = True, validators = [validate_password])
    confirm_password = serializers.CharField(write_only = True, required = True)
    
    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')
        
    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password':"Пароли отличаются"})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class UserSerializer(serializers.ModelSerializer):
    books = MangasSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id','username','date_of_birth','profile_image','description', 'email', 'books')