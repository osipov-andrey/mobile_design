from django.contrib import admin

# Register your models here.
from .models import Application, Version, Screen, Category, Developer


class ScreenInLine(admin.TabularInline):
    model = Screen


class VersionAdmin(admin.ModelAdmin):
    list_display = ('application', 'number', 'published', 'description')
    list_display_links = ('application', 'number',)
    fields = ('number', 'published', 'description')
    inlines = (ScreenInLine, )


class VersionInLine(admin.TabularInline):
    model = Version


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'developer', 'description', 'created_at')
    list_display_links = ('name',)
    fields = (('name', 'developer',), 'description', 'categories')
    inlines = (VersionInLine,)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name', )


class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Developer, DeveloperAdmin)