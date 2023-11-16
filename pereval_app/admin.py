from django.contrib import admin

# Register your models here.

from .models import PerevalAdded, Users, Coords, Season, PerevalImage

admin.site.register(Users)
admin.site.register(PerevalAdded)
admin.site.register(Coords)
admin.site.register(Season)
admin.site.register(PerevalImage)