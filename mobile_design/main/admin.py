from django.contrib import admin

# Register your models here.
from .models import Application, Version, Screen


class ScreenInLine(admin.TabularInline):
    model = Screen


class VersionAdmin(admin.ModelAdmin):
    list_display = ('application', 'number', 'published', 'description')
    list_display_links = ('number',)
    fields = ('number', 'published', 'description')
    inlines = (ScreenInLine, )


class VersionInLine(admin.TabularInline):
    model = Version


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'description', 'created_at')
    list_display_links = ('name',)
    fields = (('name', 'developer',), 'description', 'categories')
    inlines = (VersionInLine,)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Version, VersionAdmin)