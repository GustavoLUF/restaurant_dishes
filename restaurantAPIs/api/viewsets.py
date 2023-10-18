from rest_framework import viewsets, status
from restaurantAPIs.api import serializers
from restaurantAPIs import models
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Avg


class EnderecoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.EnderecoSerializer
    queryset = models.Endereco.objects.all()

class RestauranteViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RestauranteSerializer
    queryset = models.Restaurante.objects.all()

class PratoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.PratoSerializer
    queryset = models.Prato.objects.all()

    @action(detail=True, methods=['get'])
    def calcular_nota(self, request, pk=None):
        prato = self.get_object()
        media = prato.rating.aggregate(Avg('nota'))
        return Response({'Média de Notas': media['nota__avg']})

        
class RatingViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RatingSerializer
    queryset = models.Rating.objects.all()
