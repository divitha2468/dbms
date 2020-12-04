from django.contrib import admin

# Register your models here.

from.models import parent,orphan,donor,donation,adoption
admin.site.register(parent)
admin.site.register(orphan)
admin.site.register(donor)
admin.site.register(donation)
admin.site.register(adoption)