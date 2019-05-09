from datetime import date

from django.contrib.auth.models import User
from django.core.mail import EmailMessage


from rest_framework import generics
from rest_framework.decorators import permission_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
import sys

sys.path.append("..")

from seguridad.views import IsAuthenticatedOrPost
from .serializers import ArchivoSerializer, IpsFileSerializers

from .models import File, IpsFiles

from .tasks import orc

from ipware import get_client_ip

from django.contrib.gis.geoip2 import GeoIP2

from .utils import fileIpCreate, servicioTraza, fileCreate


@permission_classes([IsAuthenticatedOrPost])
class FileView(generics.ListCreateAPIView):
    queryset = File.objects.all()
    serializer_class = ArchivoSerializer

    def post(self, request, *args, **kwargs):
        if not request.data.get('id'):
            print('[-][-][-] No lleva id ')
            file_serializer = ArchivoSerializer(data=request.data)
            if file_serializer.is_valid():

                f = file_serializer.save()

                fileIpCreate(request, f)

                proceso = file_serializer.data.get('proceso')
                nombre: str = file_serializer.data.get('documento').__str__()


                nombre = nombre.split('/')[-1]

                # TODO leer proceso de los datos de entrada y configurar orc
                text = orc.delay(nombre, proceso)
        else:
            print('[+][+][+] Lleva id ')

            proceso = self.request.data.get('proceso')
            nombre: str = self.request.data.get('documento')
            text = orc.delay(nombre, proceso)

        text = text.get()


        salida = {
            "salida": text,
        }

        servicioTraza(request, salida, FileView.__name__)

        return Response(salida, status=status.HTTP_201_CREATED)



class RequestForMonth(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion__year=date.today().year, fecha_conexion__month=date.today().month)


class RequestForDay(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion=date.today())


class RequestForYear(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.filter(fecha_conexion__year=date.today().year)


class CoordenadasWithRequest(generics.ListAPIView):
    serializer_class = IpsFileSerializers
    queryset = IpsFiles.objects.all()

    def get(self, request, *args, **kwargs):
        salida = []
        for ip in IpsFiles.objects.all():
            salida.append({'usuario': ip.usuario, 'lat': ip.lat, 'lon': ip.lon})

        servicioTraza(request, salida, CoordenadasWithRequest.__name__)

        return Response(salida, status=status.HTTP_200_OK)





