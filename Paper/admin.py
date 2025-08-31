from django.contrib import admin
from .models import CustomAdmin
# Register your models here.


class MyAdmin(admin.ModelAdmin):
    model = CustomAdmin
    list_display = ['username','email','role','is_staff','is_superuser']
admin.site.register(MyAdmin,CustomAdmin)
    