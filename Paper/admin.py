from django.contrib import admin

# Register your models here.
# from .models import CustomAdmin
# Register your models here.
from .models import FeedBack

# class MyAdmin(admin.ModelAdmin):
#     model = CustomAdmin
#     list_display = ['username','email','role','is_staff','is_superuser']
# admin.site.register(CustomAdmin,MyAdmin)
    
class Sendfeedback(admin.ModelAdmin):
    model = FeedBack
    list_display = ['name','email','phone']
    search_fields = ['name','email','phone','message']
admin.site.register(FeedBack,Sendfeedback)    
    