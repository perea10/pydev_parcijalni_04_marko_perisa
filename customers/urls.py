from django.urls import path
from .views import CustomerListView, CustomerCreateView, CustomerUpdateView

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer_list'),
    path('new/', CustomerCreateView.as_view(), name='customer_create'),
    path('<int:pk>/edit/', CustomerUpdateView.as_view(), name='customer_update'),
]
