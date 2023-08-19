from django.db import models
from apps.authors.models import Authors
from apps.users.models import User
# Create your models here.

class Category(models.Model):
    category_mangas = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_mangas
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
class Mangas(models.Model):
    name = models.CharField(max_length=100)
    author_manga = models.ForeignKey(Authors, on_delete=models.CASCADE, related_name='author_manga')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_mangas')
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_manga',blank=True, null=True)
    created = models.DateField()
    manga_photo = models.FileField(upload_to='mangas_photo/', verbose_name="Фото манги")
    manga_description = models.TextField(max_length=2000)
    manga_pdf = models.FileField(upload_to ='mangas_pdf')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Манга'
        verbose_name_plural = 'Манги'