from django.db import models
from .tool_type import ToolType

class ArtworkTool(models.Model):
    name = models.CharField(max_length=255, unique=True)
    type = models.ForeignKey(ToolType, on_delete=models.CASCADE, related_name='tools')
    description = models.TextField()
    icon = models.ImageField(upload_to='icons/', blank=True, null=True)
    source = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Tool"
        verbose_name_plural = "Tools"
        ordering = ['name']
        
    def __str__(self):
        return self.name