from django.contrib import admin
import csv
from django.http import HttpResponse

from .models import *


@admin.action(description='Експорт в csv')
def export_as_csv(self, request, queryset):

    meta = self.model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])
    return response


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'telegram_username', 'balance']

class ProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'proxy_type', 'proxy_value']
    actions = [export_as_csv]

class All_transactions_trx_trc20Admin(admin.ModelAdmin):
    list_display = ['hash', 'value']

admin.site.register(User, UserAdmin)
admin.site.register(All_transactions_trx_trc20, All_transactions_trx_trc20Admin)
admin.site.register(Proxy, ProxyAdmin)