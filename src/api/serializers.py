from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class All_transactions_trx_trc20_Serializer(serializers.ModelSerializer):
    class Meta:
        model = All_transactions_trx_trc20
        fields = '__all__'


class Proxy_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Proxy
        fields = '__all__'