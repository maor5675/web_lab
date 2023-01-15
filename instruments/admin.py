from django.contrib import admin

from instruments.models import Phonebrand,Phonetype,Phone,Malfunction_type,Malfunction,Price,handled_by

admin.site.register(Phonebrand)
admin.site.register(Phonetype)
admin.site.register(Phone)
admin.site.register(Malfunction_type)
admin.site.register(Malfunction)
admin.site.register(Price)
admin.site.register(handled_by)



