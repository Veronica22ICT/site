from django.contrib import admin
from django.contrib.admin import register
from knife.models import Knife, Care, Repair, Order

admin.site.register(Order)

@register(Knife)
class KnifeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available' )
    list_per_page = 7

@register(Care)
class CareAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available' )
    list_per_page = 7

@register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available' )
    list_per_page = 7

