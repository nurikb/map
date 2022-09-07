from django.contrib.gis import admin

from .models import WorldBorder


class WorldAdmin(admin.GISModelAdmin):
    search_fields = ("name",)


admin.site.register(WorldBorder, WorldAdmin)

# Register your models here.
