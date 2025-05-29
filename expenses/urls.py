from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_expenses, name='create_expenses'),
]
