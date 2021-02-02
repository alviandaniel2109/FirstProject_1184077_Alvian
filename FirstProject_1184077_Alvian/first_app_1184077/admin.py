from django.contrib import admin

# Register your models here.
from first_app_1184077.models import AccessRecord,Topic,Webpage


#
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)