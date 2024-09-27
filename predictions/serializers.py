from rest_framework import serializers
from .models import Region, City, District, UserProfile

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