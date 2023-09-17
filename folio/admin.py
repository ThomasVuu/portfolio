from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.About)
class AboutAdmin(admin.ModelAdmin):
    pass

class ProjectImageInline(admin.TabularInline):
    model = models.ProjectImage
    readonly_fields = ('id',)

@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    pass

