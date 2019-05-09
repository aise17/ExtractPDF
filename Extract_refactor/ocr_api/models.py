from django.db import models
import uuid
from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField

from ckeditor.fields import RichTextField, CKEditorWidget

import sys
sys.path.append('..')

from anuncios.models import Bono


class Salida():
    ok = False
    errores = []
    resut_text_ocr = ''



class File(models.Model):
    PROCESOS = (
        ('B', 'B'),
        ('T', 'T'),
        ('TB', 'TB'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.TextField(max_length=255, blank=True)
    documento = models.FileField('Uploaded pdf')
    dateTimeUp = models.DateTimeField(auto_now=True)
    proceso = models.TextField(choices=PROCESOS, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.descripcion


class IpsFiles(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    fecha_conexion = models.DateField(auto_now=True)
    ip = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    lat = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    is_routeable = models.NullBooleanField(null=True, blank=True)

    def __str__(self):
        return self.ip


class Traza(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    funcion_llamada = models.CharField(max_length=255, blank=True)
    datos_in = JSONField()
    datos_out = JSONField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha_creacion = models.DateField(auto_now=True)
    error = models.BooleanField(default=False)


class BonoUsuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bono = models.ForeignKey(Bono, on_delete=models.CASCADE, null=True)
    activado = models.BooleanField(default=True)
    fecha_creacion = models.DateField(auto_now=True)

