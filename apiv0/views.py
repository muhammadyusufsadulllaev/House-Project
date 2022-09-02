from home.models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

class RegionViewSet(viewsets.ModelViewSet):

    queryset = Region.objects.all()
    serializer_class = RegionSerializer
    pagination_class = PageNumberPagination


class DistrictViewSet(viewsets.ModelViewSet):

    queryset = District.objects.all()
    serializer_class = DistrictSerializer
    pagination_class = PageNumberPagination


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class RepairViewSet(viewsets.ModelViewSet):

    queryset = Repair.objects.all()
    serializer_class = RepairSerializer
    pagination_class = PageNumberPagination


class CurrencyViewSet(viewsets.ModelViewSet):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    pagination_class = PageNumberPagination


class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = PageNumberPagination


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    pagination_class = PageNumberPagination


class HouseViewSet(viewsets.ModelViewSet):

    queryset = House.objects.all()
    serializer_class = HouseSerializer
    pagination_class = PageNumberPagination


class RoomsViewSet(viewsets.ModelViewSet):

    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer
    pagination_class = PageNumberPagination


class PaymentViewSet(viewsets.ModelViewSet):

    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    pagination_class = PageNumberPagination


class RentalViewSet(viewsets.ModelViewSet):

    queryset = Rental.objects.all()
    serializer_class = RentalSerializer
    pagination_class = PageNumberPagination


class HistoryViewSet(viewsets.ModelViewSet):

    queryset = History.objects.all()
    serializer_class = HistorySerializer
    pagination_class = PageNumberPagination

