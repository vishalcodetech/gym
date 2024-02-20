from django.contrib import admin
from .models import Service
#Register your models here.
from .models import *
admin.site.register(Contact)
admin.site.register(Service)
