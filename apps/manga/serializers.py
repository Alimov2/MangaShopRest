from rest_framework import serializers
from apps.manga.models import Category, Mangas

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        
class MangasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mangas
        fields = ('id', 'name','created', 'price','manga_photo', 'manga_description', 'manga_pdf', 'author_manga', 'category','owner','user_info')
        
    user_info = serializers.SerializerMethodField()
    def get_user_info(self, obj):
        qs = obj.owner
        data = {}
        data.setdefault('id',qs.id)
        data.setdefault('username',qs.username)
        if qs.profile_image:
            data.setdefault('profile_image',qs.profile_image)
        else:
            data.setdefault('profile_image','')
        return data