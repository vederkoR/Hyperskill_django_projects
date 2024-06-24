from django.shortcuts import render
from .models import Bike


def index(request):
    bikes = Bike.objects.all()
    return render(request, 'shop/index.html', {'bikes': bikes})
