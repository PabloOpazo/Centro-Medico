from datetime import date
from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.db.models.fields.related import ForeignKey

class Especialidade(models.Model):
    nome = models.CharField(verbose_name="Nombre", max_length=200)
    
    def __str__(self):
        return f'{self.nome}'
    
class Medico(models.Model):
    nome = models.CharField(verbose_name="Nombre", max_length=200)
    email = models.EmailField(verbose_name="Email")
    RUT = models.CharField(verbose_name="RUT", max_length=200)
    chilean_phone_regex = RegexValidator(
    regex=r'^\+\d{3} \d{4} \d{4}$',
    message="El número debe estar en el formato: '+569 1234 5678'.")
    telefone = models.CharField(
        verbose_name="Teléfono",
        validators=[chilean_phone_regex],
        max_length=15,  # Ajusta la longitud máxima para el formato chileno
        null=True,
        blank=True
    )
    especialidad = ForeignKey(Especialidade,
                               on_delete=models.CASCADE,
                               related_name='medicos')
    
    def __str__(self):
        return f'{self.nome}'

def validar_dia(value):
    today = date.today()
    weekday = date.fromisoformat(f'{value}').weekday()

    if value < today:
        raise ValidationError('No es posible elegir una fecha tardía.')
    if (weekday == 5) or (weekday == 6):
        raise ValidationError('Elija un día hábil de la semana.')

class Agenda(models.Model):
    medico = ForeignKey(Medico, on_delete=models.CASCADE, related_name='agenda')
    dia = models.DateField(help_text="Introduzca una fecha para el calendario", validators=[validar_dia])
    
    HORARIOS = (
        ("1", "07:00 a 08:00"),
        ("2", "08:00 a 09:00"),
        ("3", "09:00 a 10:00"),
        ("4", "10:00 a 11:00"),
        ("5", "11:00 a 12:00"),
    )
    horario = models.CharField(max_length=10, choices=HORARIOS)
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Usuario', 
        on_delete=models.CASCADE
    )
    class Meta:
        unique_together = ('horario', 'dia')
        
    def __str__(self):
        return f'{self.dia.strftime("%b %d %Y")} - {self.get_horario_display()} - {self.medico}'