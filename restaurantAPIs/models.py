from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Endereco(models.Model):
    endereco = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)

    def __str__(self):
        return self.endereco

class Restaurante(models.Model):
    nome = models.CharField(max_length=255)
    endereco = models.ForeignKey(Endereco, on_delete=models.SET_NULL, null=True, related_name="restaurante")

    def __str__(self):
        return self.nome

class Prato(models.Model):
    nome = models.CharField(max_length=255)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name="pratos")
    descricao = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome
    
class Rating(models.Model):
    prato = models.ForeignKey(Prato,  on_delete=models.CASCADE, related_name="rating")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="rating")
    nota = models.PositiveSmallIntegerField(default=None, null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"Nota {self.nota} dada ao prato {self.prato.nome}, pelo usuário {self.usuario.username}"