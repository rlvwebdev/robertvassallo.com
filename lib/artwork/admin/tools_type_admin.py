from django.contrib import admin
from lib.artwork.models.tool_type import ToolType

@admin.register(ToolType)
class ToolTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)