from django.contrib import admin
from .models import Photo, categories,location

# Register your models here.

class categoriesAdmin(admin.ModelAdmin):
    filter_horizontal =('location',)

admin.site.register(Photo)
admin.site.register(categories,categoriesAdmin)
admin.site.register(location)
