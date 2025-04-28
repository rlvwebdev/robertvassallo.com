from django.contrib import admin
from django.utils.html import format_html
from lib.artwork.models.entry import Entry
from lib.artwork.models.entry_comments import EntryComment

class EntryCommentInline(admin.TabularInline):
    model = EntryComment
    extra = 1

@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_at', 'updated_at', 'hero_image_preview', 'thumbnail_image_preview')
    search_fields = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)
    filter_horizontal = ('tools_used',)  # Display tools_used as checkboxes
    inlines = [EntryCommentInline]  # Add comments inline

    def hero_image_preview(self, obj):
        if obj.hero_image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.hero_image.url)
        return "No Image"
    hero_image_preview.short_description = 'Hero Image Preview'

    def thumbnail_image_preview(self, obj):
        if obj.thumbnail_image:
            return format_html('<img src="{}" style="max-height: 100px;" />', obj.thumbnail_image.url)
        return "No Image"
    thumbnail_image_preview.short_description = 'Thumbnail Image Preview'