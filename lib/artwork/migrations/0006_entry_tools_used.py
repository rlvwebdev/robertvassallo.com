# Generated by Django 5.2 on 2025-04-27 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0005_artworktool_source'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tools_used',
            field=models.ManyToManyField(blank=True, related_name='entries', to='artwork.artworktool'),
        ),
    ]
