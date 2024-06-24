from django.contrib import admin
from .models import Frame, Seat, Tire, Basket, Bike, Order


@admin.register(Frame)
class AdminFrame(admin.ModelAdmin):
    fields = ('color', 'quantity')
    list_display = ('color', 'quantity')


@admin.register(Seat)
class AdminSeat(admin.ModelAdmin):
    fields = ('color', 'quantity')
    list_display = ('color', 'quantity')


@admin.register(Tire)
class AdminTire(admin.ModelAdmin):
    fields = ('type', 'quantity')
    list_display = ('type', 'quantity')


@admin.register(Basket)
class AdminBasket(admin.ModelAdmin):
    fields = ('quantity',)
    list_display = ('quantity',)


@admin.register(Bike)
class AdminBike(admin.ModelAdmin):
    fields = ('name', 'description', 'has_basket', 'frame', 'tire', 'seat',)
    list_display = ('name', 'description', 'has_basket', 'frame', 'tire', 'seat',)


@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    fields = ('name', 'surname', 'phone_number', 'status', 'bike')
    list_display = ('name', 'surname', 'phone_number', 'status', 'bike')
    readonly_fields = ('name', 'surname', 'phone_number', 'status', 'bike')
