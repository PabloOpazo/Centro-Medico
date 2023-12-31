# Generated by Django 4.0.1 on 2023-10-30 19:00

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='telefono',
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefone',
            field=models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="El número debe estar en este formato:                         '+999 99999999'.", regex='^\\+\\d{3} \\d{8}$')], verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='RUT',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='sexo',
            field=models.CharField(choices=[('MAS', 'Masculino'), ('FEM', 'Femenino'), ('N/A', 'Otro')], max_length=9),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
