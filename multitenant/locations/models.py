from django.db import models
from tenant_schemas.models import TenantMixin


# Create your models here.
class Library(TenantMixin):
    name = models.CharField(max_length=100)
    created_on = models.DateField(auto_now_add=True)
    auto_create_schema = True
