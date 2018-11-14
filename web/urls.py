from django.urls import path
from web import views


urlpatterns = [
    path('', views.index, name='index'),
    path('listings/', views.ListingListView.as_view(), name='listing-list'),
    path('listing/<int:pk>', views.ListingDetailView.as_view(), name='listing-detail')
]

