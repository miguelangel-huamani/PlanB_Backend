from django.urls import path
from .views import CategoryListCreate, CategoryRetrieveUpdateDestroy, AuctionListCreate, AuctionRetrieveUpdateDestroy, BidListCreate, BidRetrieveUpdateDestroy, UserAuctionListView


app_name="auctions"
urlpatterns = [
    #Auctions URLs
    path('', AuctionListCreate.as_view(), name='auction-list-create'),
    path('<int:pk>/', AuctionRetrieveUpdateDestroy.as_view(), name='auction-detail'),

    #Categories URLs
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-detail'),

    #Bis URLs
    path('<int:auction_id>/bids/', BidListCreate.as_view(), name='bid-list-create'),
    path('<int:auction_id>/bids/<int:pk>/', BidRetrieveUpdateDestroy.as_view(), name='bid-detail'),

    path('users/', UserAuctionListView.as_view(), name='action-from-users'),
]