from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models.signals import post_save
from django.db import connection

from myapp import models

admin.site.register(models.Tenant)
admin.site.register(models.TenantUser, UserAdmin)

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'tel', 'email', 'tenant')
    list_display_links = ('id', 'name')

def on_create_tenant(sender, instance, created, **kwargs):
    if created:
        tenant_role = 'tn' + instance.id.hex
        with connection.cursor() as cursur:
            cursur.execute(f'CREATE ROLE {tenant_role}')
            cursur.execute(f'GRANT tenantuser TO {tenant_role}')

post_save.connect(on_create_tenant, sender=models.Tenant)