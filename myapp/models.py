import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Tenant(models.Model):
    
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    tenant_key = models.CharField(_("TenantId"), max_length=50, unique=True)
    tenant_name = models.CharField(_("TenantName"), max_length=100)

    class Meta:
        db_table = 'tenants'
        verbose_name = _("Tenant")
        verbose_name_plural = _("Tenants")

    def __str__(self):
        return self.tenant_name

    def get_absolute_url(self):
        return reverse("Tenant_detail", kwargs={"pk": self.pk})
    
    def get_role(self):
        return 'tn' + self.id.hex

class TenantUser(AbstractUser):
    
    id = models.UUIDField(_("ID"), primary_key=True, editable=False, default=uuid.uuid4)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tenant_users'
        verbose_name = _("TenantUser")
        verbose_name_plural = _("TenantUsers")

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("TenantUser_detail", kwargs={"pk": self.pk})

class Customer(models.Model):
    
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    tel = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)

    class Meta:
        db_table = 'customer'
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Customer_detail", kwargs={"pk": self.pk})
