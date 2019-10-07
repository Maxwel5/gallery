from django.contrib import admin
from .models import Photo, categories,location

# Register your models here.
admin.site.register(Photo)
admin.site.register(categories)
admin.site.register(location)
