
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.generic import RedirectView
from django.conf.urls.static import static
from rest_framework import routers
from apps.authors.views import AuthorsViewSet
from apps.manga.views import CategoryViewSet, MangasViewSet
from apps.users.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'authors', AuthorsViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'manga', MangasViewSet)

api_urlpatterns = [
    path('users/', include('apps.users.urls')),
    path('manga/', include('apps.manga.urls')),
    path('authors/', include('apps.authors.urls')),
]
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api_urlpatterns)),
    path('api/', include(router.urls)),
    path('',RedirectView.as_view(url='/api/')),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)