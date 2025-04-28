from django.contrib import admin
from lib.artwork.models.tools import ArtworkTool

@admin.register(ArtworkTool)
class ArtworkToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'description')
    search_fields = ('name', 'type', 'description')
    list_filter = ('type',)
    ordering = ('name',)