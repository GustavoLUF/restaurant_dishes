from rest_framework import serializers
from restaurantAPIs import models

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Endereco
        fields = '__all__'

class RestauranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurante
        fields = '__all__'

class PratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Prato
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Rating
        fields = '__all__'