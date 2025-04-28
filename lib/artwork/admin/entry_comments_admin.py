from django.contrib import admin
from ..models.entry_comments import EntryComment

@admin.register(EntryComment)
class EntryCommentAdmin(admin.ModelAdmin):
    list_display = ('entry', 'user', 'text', 'created_at', 'updated_at')
    search_fields = ('text', 'user__username', 'entry__title')
    list_filter = ('created_at', 'updated_at')