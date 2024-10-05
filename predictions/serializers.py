from rest_framework import serializers
from .models import Region, City, District, UserProfile
from django.contrib.auth.models import User

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['gender', 'age', 'city']

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

def create(self, validated_data):
    user = User(
        username=validated_data['username'],
        email=validated_data['email'],
    )
    user.set_password(validated_data['password'])
    user.save