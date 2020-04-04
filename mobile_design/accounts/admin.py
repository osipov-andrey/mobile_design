from django.contrib import admin

# Register your models here.
from .models import AdvUser


class AdvUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(AdvUser, AdvUserAdmin)