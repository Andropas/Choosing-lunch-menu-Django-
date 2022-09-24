from django.contrib import admin

from .models import Restaurant, Menu, Employee

class MenuInLine(admin.TabularInline):
    model = Menu
    extra = 0

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [MenuInLine]
    list_display = ('restaurant_name', 'get_today_menu')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Employee)