from django.db import models
from django.urls import reverse_lazy
from .models import Customer
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
class CustomerListView(ListView):
    model = Customer


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_list.html'


class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'customers/customer_list.html'
    success_url = reverse_lazy('customers:customer_list')


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'customers/customer_list.html'
    success_url = reverse_lazy('customers:customer_list')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_list.html'
    success_url = reverse_lazy('customers:customer_list')
