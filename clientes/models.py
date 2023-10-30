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
    
    phone_regex = RegexValidator(
        regex = r'^\+\d{3} \d{8}$',
        message="El número debe estar en este formato: \
                        '+999 99999999'.")

    telefone = models.CharField(verbose_name="Teléfono",
                                validators=[phone_regex],
                                max_length=17, null=True, blank=True)
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
