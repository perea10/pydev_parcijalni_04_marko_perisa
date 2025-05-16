from django.shortcuts import render
from .models import Offer
from django.views.generic import ListView

class OfferListView(ListView):
    offers = Offer.objects.all().select_related('customer', 'user')
    
