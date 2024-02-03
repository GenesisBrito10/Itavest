from rest_framework import serializers
from .models import Bordado


class BordadoSerializer(serializers.ModelSerializer):
    Cadastrado_por = serializers.CharField(source='user.username', read_only=True)
    Data = serializers.DateTimeField(format="%d-%m-%Y %H:%M", read_only=True)

    class Meta:
        model = Bordado
        fields = '__all__'
