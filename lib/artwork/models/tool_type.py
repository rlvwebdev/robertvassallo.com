from django.db import models

class ToolType(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __str__(self):
        return self.name