from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('news/<int:link>/', views.NewsView.as_view(), name='news')
]
