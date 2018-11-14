from django.shortcuts import render
from django.views import generic
from web.models import Listing, ListingImage


def index(request):
    return render(request, 'index.html')


class ListingDetailView(generic.DetailView):
    model = Listing


class ListingListView(generic.ListView):
    model = Listing
