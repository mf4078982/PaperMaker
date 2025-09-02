from django.contrib import admin

# Register your models here.
from .models import CustomAdmin
# Register your models here.


class MyAdmin(admin.ModelAdmin):
    model = CustomAdmin
    list_display = ['username','email','role','is_staff','is_superuser']
admin.site.register(CustomAdmin,MyAdmin)
    
