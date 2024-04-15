from django.contrib import admin
from .models import AdminDataBase ,Customer 
# Register your models here.
class M(admin.ModelAdmin):
  list_display = ("id","name","lname","email","age","identity","image")


admin.site.register(AdminDataBase)
admin.site.register(Customer,M)