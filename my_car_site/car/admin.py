import imp
from django.contrib import admin
from car.models import Car
# Register your models here.
class MyCarAdmin(admin.ModelAdmin):
    fieldsets=[
        ('YEAR INFORMATION', {'fields':['year']}),
        ('CAR INFORMATION', {'fields':['brand']})
    ]


admin.site.register(Car,MyCarAdmin)