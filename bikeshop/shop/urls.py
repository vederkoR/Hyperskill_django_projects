from django.urls import path
from . import views

urlpatterns = [
    path("bikes/", views.index, name="index"),
    path("bikes/<int:pk>/", views.BikeView.as_view(), name="bike"),
    path("order/<int:order_number>/", views.order_info, name="order")
]
