# Generated by Django 3.2.3 on 2021-06-18 02:44

from random import choice
from django.db import migrations
from myapp.admin import on_create_tenant


def migrate_data(apps, schema_editor):
    Tenant = apps.get_model('myapp', 'Tenant')
    TenantUser = apps.get_model('myapp', 'TenantUser')
    Customer = apps.get_model('myapp', 'Customer')

    # Admin
    TenantUser.objects.create_superuser('admin', password='admin_pass')

    # Tenant1
    t1 = Tenant.objects.create(tenant_key='xxx', tenant_name='XXX Inc.')
    on_create_tenant('', t1, True)
    TenantUser.objects.create_superuser('aaa', password='aaa_pass', tenant=t1)
    TenantUser.objects.create_superuser('bbb', password='bbb_pass', tenant=t1)

    # Tenant2
    t2 = Tenant.objects.create(tenant_key='yyy', tenant_name='YYY Com')
    on_create_tenant('', t2, True)
    TenantUser.objects.create_superuser('ccc', password='ccc_pass', tenant=t2)

    # Customers
    for i in range(10):
        t = choice([t1, t2])
        dmy = chr(ord('a')+i)*2
        Customer.objects.create(
            tenant=t,
            **{k: f"{k} {dmy}" for k in ('name', 'address', 'tel', 'email')}
        )


def reverse_data(apps, schema_editor):
    Tenant = apps.get_model('myapp', 'Tenant')
    Tenant.objects.filter(tenant_key__in=['beproud', 'cmscom']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_setup_roles'),
    ]

    operations = [
        migrations.RunPython(
            migrate_data,
            reverse_code=reverse_data
        ),
    ]