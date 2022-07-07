from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *


router = routers.SimpleRouter()
router.register(r'user', User_Viev)
router.register(r'all_transactions_trx_trc20', All_transactions_trx_trc20_Viev)
router.register(r'proxy', Proxy_Viev)
router.register('user_secret_key', User_Secret_key_Viev)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]
