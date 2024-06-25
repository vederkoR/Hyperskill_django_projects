from django.shortcuts import render
from django.views import View

from .models import Bike


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'shop/index.html', {'bikes': bikes})


class BikeView(View):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        bike = Bike.objects.filter(pk=pk).first()
        return render(request, 'shop/bike_details.html', context={'bike': bike})
