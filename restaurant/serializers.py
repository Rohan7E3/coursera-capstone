from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Menu, Booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta():
        model = Menu
        fields = ['id', 'title', 'price', 'inventory']
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Booking
        fields = ['id', 'name', 'number_of_guests', 'booking_date']

class GroupNameField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name

class UserSerializer(serializers.ModelSerializer):
    groups = GroupNameField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']