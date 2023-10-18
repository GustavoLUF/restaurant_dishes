from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from restaurantAPIs.api import viewsets
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

route = routers.DefaultRouter()

route.register(r'Endereço', viewsets.EnderecoViewSet, basename='endereco')
route.register(r'Restaurante', viewsets.RestauranteViewSet, basename='restaurante')
route.register(r'Prato', viewsets.PratoViewSet, basename='prato')
route.register(r'Rating', viewsets.RatingViewSet, basename='rating')

schema_view = get_schema_view(
   openapi.Info(
      title="Restaurant_Dishes APIs",
      default_version='v1.0',
      description="",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
]

urlpatterns += [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
