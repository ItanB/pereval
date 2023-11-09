from django.contrib import admin

# Register your models here.

from .models import PerevalAdded, Users

admin.site.register(Users)
admin.site.register(PerevalAdded)

