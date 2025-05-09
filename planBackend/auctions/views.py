from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from .models import Category, Auction, Bid
from .serializers import CategoryListCreateSerializer, CategoryDetailSerializer, AuctionListCreateSerializer, AuctionDetailSerializer, BidListCreateSerializer, BidDetailSerializer
from django.db.models import Q

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

#PERMISOS
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrAdmin

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListCreateSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]  # Solo admin puede crear/modificar categorías

class CategoryRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAdminUser]  # Solo admin puede editar/eliminar categorías

class AuctionListCreate(generics.ListCreateAPIView):
    serializer_class = AuctionListCreateSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]  # Cualquier usuario autenticado puede crear subastas

    def get_queryset(self): 
        queryset = Auction.objects.all()
        params = self.request.query_params

        search = params.get('search')
        category = params.get('category')

        if search and len(search) <1: # validación para comprobar que la querysearch sea de como mínimo 1 caracter
            raise ValidationError("La búsqueda debe tener al menos 1 carácter",             
                                    code=status.HTTP_400_BAD_REQUEST)


        if search:
            # Aplicar el filtro tanto a la descripción como al título
            queryset = queryset.filter(Q(title__icontains=search) | Q(description__icontains=search)) 

        if category:
            queryset = queryset.filter(category__id=category)

        return queryset


class AuctionRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionDetailSerializer
    permission_classes = [IsOwnerOrAdmin]  # Solo dueño o admin puede modificar/eliminar

class BidListCreate(generics.ListCreateAPIView):
    serializer_class = BidListCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        auction_id = self.kwargs['auction_id']
        return Bid.objects.filter(auction__id=auction_id)

    def perform_create(self, serializer):
        auction_id = self.kwargs['auction_id']
        auction = Auction.objects.get(pk=auction_id)
        serializer.save(bidder=self.request.user, auction=auction)

class BidRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BidDetailSerializer
    permission_classes = [IsOwnerOrAdmin]  # Solo dueño de la puja o admin puede modificar/eliminar

    def get_queryset(self):
        auction_id = self.kwargs['auction_id']
        return Bid.objects.filter(auction__id=auction_id)

class UserAuctionListView(APIView):
    # Listar todas las subastas asociadas a un usuario
    permission_classes = [IsAuthenticated]  # Correcto - solo usuarios autenticados

    def get(self, request, *args, **kwargs):
        # Obtener las subastas del usuario autenticado
        user_auctions = Auction.objects.filter(auctioneer=request.user)
        serializer = AuctionListCreateSerializer(user_auctions, many=True)
        return Response(serializer.data)

class UserBidListView(APIView):
    # Registrar las pujas de un usuario en completo
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user_bids = Bid.objects.filter(bidder=request.user)
        serializer = BidListCreateSerializer(user_bids, many=True)
        return Response(serializer.data)

