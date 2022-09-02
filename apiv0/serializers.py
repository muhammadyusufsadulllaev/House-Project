from rest_framework import serializers
from home.models import *


class RegionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Region
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = District
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'


class RepairSerializer(serializers.ModelSerializer):

    class Meta:
        model = Repair
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Currency
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        fields = '__all__'


class HouseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = House
        fields = '__all__'


class RoomsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rooms
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Payment
        fields = '__all__'


class RentalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rental
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = History
        fields = '__all__'




