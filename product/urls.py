from django.contrib import admin
from django.urls import path, include
from .views import ProductView

urlpatterns = [
    path('<int:product_id>/', ProductView.as_view()),
    path('', ProductView.as_view()),
]