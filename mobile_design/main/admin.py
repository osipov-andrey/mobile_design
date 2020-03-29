from django.contrib import admin

# Register your models here.
from .models import Application, Version, Screen, Category, Developer, SubElement, \
    SuperElement, SubPattern, SuperPattern
from .forms import SubElementForm, SubPatternForm


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


class SubElementInLine(admin.TabularInline):
    model = SubElement


class SuperElementAdmin(admin.ModelAdmin):
    exclude = ('super_element',)
    inlines = (SubElementInLine,)


class SubElementAdmin(admin.ModelAdmin):
    form = SubElementForm


class SubPatternInLine(admin.TabularInline):
    model = SubPattern


class SuperPatternAdmin(admin.ModelAdmin):
    exclude = ('super_pattern',)
    inlines = (SubPatternInLine,)


class SubPatternAdmin(admin.ModelAdmin):
    form = SubPatternForm


class ScreenAdmin(admin.ModelAdmin):
    list_display = ('name', 'application')
    list_display_links = ('name', 'application')


admin.site.register(Screen, ScreenAdmin)
admin.site.register(SubElement, SubElementAdmin)
admin.site.register(SuperElement, SuperElementAdmin)
admin.site.register(SubPattern, SubPatternAdmin)
admin.site.register(SuperPattern, SuperPatternAdmin)
admin.site.register(Application, ApplicationAdmin)
admin.site.register(Version, VersionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Developer, DeveloperAdmin)