from rest_framework import serializers
from .models import Menu, Booking
from django.utils.timezone import now


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"

    # Custom field-level validation
    def validate_no_of_guests(self, value):
        if value <= 0:
            raise serializers.ValidationError("Number of guests must be greater than 0.")
        return value
    """ The validate_<fieldname> method in a
    Django REST Framework (DRF) serializer is a field-specific validation hook. """
    # Custom object-level validation
    def validate(self, data):
        if data['booking_date'] < now():
            raise serializers.ValidationError("Booking date cannot be in the past.")
        return data

class MenuSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Menu
        fields = "__all__"