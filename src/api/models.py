from django.db import models


class User(models.Model):
    telegram_id = models.IntegerField(unique=True, null=True)
    telegram_username = models.CharField(max_length=250, null=True)
    secret_key = models.CharField(max_length=250, unique=True, null=True)
    balance = models.FloatField(max_length=12, null=True)

    def __str__(self):
        return self.telegram_username


class All_transactions_trx_trc20(models.Model):
    hash = models.CharField(max_length=250, unique=True)
    value = models.FloatField(max_length=10)

    def __str__(self):
        return self.hash

class All_transactions_usdt_trc20(models.Model):
    hash = models.CharField(max_length=250, unique=True)
    value = models.FloatField(max_length=10)

    def __str__(self):
        return self.hash


class Proxy(models.Model):
    proxy_type = models.CharField(max_length=250)
    proxy_value = models.CharField(max_length=250)

    def __str__(self):
        return self.proxy_value