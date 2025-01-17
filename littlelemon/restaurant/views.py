from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu,Booking
from .serializers import MenuSerializer,BookingSerializer
from  rest_framework.permissions import IsAuthenticated

class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()  # Fetch all menu items
    serializer_class = MenuSerializer
class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()  # Fetch all menu items
    serializer_class = MenuSerializer  # Use the MenuTable serializer


class  BookingViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class=BookingSerializer