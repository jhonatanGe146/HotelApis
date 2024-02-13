from rest_framework import serializers
from .models import persona, tipo_documento, tipo_persona

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = persona
        fields = "__all__"

class TipoUsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_persona
        fields = "__all__"

class TipoDocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = tipo_documento
        fields = "__all__"