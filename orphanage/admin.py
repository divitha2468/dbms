from django.contrib import admin

# Register your models here.

from.models import parent,adoption,donation
admin.site.register(parent)
admin.site.register(adoption)
admin.site.register(donation)