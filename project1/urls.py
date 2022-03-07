
from django.contrib import admin
from django.urls import path
from User import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('ProfileApi', views.ProfileViewSet, basename='UserProfile')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="home"),
    path('api', include(router.urls))


]
