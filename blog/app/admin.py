from django.contrib import admin
from .models import store, seller 
# Register your models here.

class storeAdmin(admin.ModelAdmin):

    list_display = ('st_name','st_location','st_Address', 'st_status')
    search_fields=('st_name', 'st_Address')
    list_filter = ('st_status','st_name')

admin.site.register(store,storeAdmin)
admin.site.register(seller)