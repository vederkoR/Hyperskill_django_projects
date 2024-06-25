from django.shortcuts import render
from django.views import View
from django import forms

from .models import Bike, Order, Basket


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'surname', 'phone_number']
        labels = {'name': 'your name:',
                  'surname': 'your surname:',
                  'phone_number': 'your phone number:'}


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'shop/index.html', {'bikes': bikes})


class BikeView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        bike = Bike.objects.filter(pk=pk).first()
        basket_quantity = Basket.objects.all().first().quantity
        available = all(
            [bike.frame.quantity >= 1,
             bike.tire.quantity >= 2,
             bike.seat.quantity >= 1,
             (not bike.has_basket or basket_quantity >= 1)])
        form = OrderForm()
        context = {'bike': bike, 'form': form, 'available': available}
        return render(request, 'shop/bike_details.html', context=context)
