from rest_framework import generics, viewsets
from django.shortcuts import render

from .serializers import *
from .models import *


class User_Viev(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'telegram_id'


class User_Secret_key_Viev(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'secret_key'

class All_transactions_trx_trc20_Viev(viewsets.ModelViewSet):
    queryset = All_transactions_trx_trc20.objects.all()
    serializer_class = All_transactions_trx_trc20_Serializer
    lookup_field = 'hash'


class Proxy_Viev(viewsets.ModelViewSet):
    queryset = Proxy.objects.all()
    serializer_class = Proxy_Serializer