from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MyModel


class MyModelAdmin(admin.ModelAdmin):
    list_display = ('uid', 'address', 'number')  # fields to display in the list view


admin.site.register(MyModel, MyModelAdmin)
