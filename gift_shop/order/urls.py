from django.urls import path, include
from order import views
from .views import checkout

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),
]