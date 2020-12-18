from django.contrib import admin

# Register your models here.

from.models import staff,orphan,donor,donation,adoption
admin.site.register(staff)
admin.site.register(orphan)
admin.site.register(donor)
admin.site.register(donation)
admin.site.register(adoption)