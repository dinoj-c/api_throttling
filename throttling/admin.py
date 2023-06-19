from django.contrib import admin
from .models import Throttle


class ThrottleAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Throttle._meta.fields]

admin.site.register(Throttle, ThrottleAdmin)
