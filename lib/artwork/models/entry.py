from django.db import models
from .tools import ArtworkTool

class Entry(models.Model):
    title = models.CharField(max_length=255)
    hero_image = models.ImageField(upload_to='hero_images/')
    thumbnail_image = models.ImageField(upload_to='thumbnail_images/')
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tools_used = models.ManyToManyField(ArtworkTool, related_name='entries', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Entry"
        verbose_name_plural = "Entries"
        ordering = ['-created_at']