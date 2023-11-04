from django.conf import settings
from django.db.models.fields.related import ForeignKey, OneToOneField
from django_cpf_cnpj.fields import CPFField
from django.core.validators import RegexValidator
from django.db import models
from medicos.models import Agenda

class Cliente(models.Model):
    SEXO = (
        ("MAS", "Masculino"),
        ("FEM", "Femenino"),
        ("N/A", "Otro")
    )
    
    sexo = models.CharField(max_length=9, choices=SEXO,)
    
    chilean_phone_regex = RegexValidator(
    regex=r'^\+\d{2} \d{4} \d{4}$',
    message="El número debe estar en el formato: '+569 1234 5678'.")
    telefone = models.CharField(
        verbose_name="Teléfono",
        validators=[chilean_phone_regex],
        max_length=15,  # Ajusta la longitud máxima para el formato chileno
        null=True,
        blank=True
    )
    RUT = models.CharField(max_length=12, )
    
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    
    def __str__(self):
        return f'{self.user.name}'
    
class Consulta(models.Model):
    agenda =  OneToOneField(Agenda, on_delete=models.CASCADE, related_name='consulta')
    cliente = ForeignKey(Cliente, on_delete=models.CASCADE, related_name='consulta')
    
    class Meta:
        unique_together = ('agenda', 'cliente')
        
    def __str__(self):
        return f'{self.agenda} - {self.cliente}'
