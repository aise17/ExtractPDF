
from rest_framework import serializers
from .models import AnuncioInferior, AnuncioSuperior, AnuncioLateral, QuienSomos, Bono, Explicacion, Faqs, \
    ExplicacionScrapy, NormasOcr, NormasScrapy


class AnuncioLateralSerializer(serializers.ModelSerializer):

    class Meta:
        model= AnuncioLateral
        fields = "__all__"


class AnuncioSuperiorSerializer(serializers.ModelSerializer):

    class Meta:
        model= AnuncioSuperior
        fields = "__all__"


class AnuncioInferiroSerializer(serializers.ModelSerializer):

    class Meta:
        model= AnuncioInferior
        fields = "__all__"


class BonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bono
        fields = "__all__"




class QuienSomosSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuienSomos
        fields = "__all__"


class ExplicaionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Explicacion
        fields = "__all__"


class ExplicaionScrapySerializer(serializers.ModelSerializer):

    class Meta:
        model= ExplicacionScrapy
        fields = "__all__"


class FaqsSerializer(serializers.ModelSerializer):

    class Meta:
        model= Faqs
        fields = "__all__"

class NormasOcrSerializer(serializers.ModelSerializer):

    class Meta:
        model= NormasOcr
        fields = "__all__"

class NomrmasScrapyerializer(serializers.ModelSerializer):

    class Meta:
        model= NormasScrapy
        fields = "__all__"