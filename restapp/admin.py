from django.contrib import admin
from .models import bigdata
# Register your models here.

@admin.register(bigdata)
class BigDataAdminModel(admin.ModelAdmin):
    #panel listeleme
    fields = ("title","text","price")
    list_display = ("title","text","price")
    list_display_links = ("text","title")
    


