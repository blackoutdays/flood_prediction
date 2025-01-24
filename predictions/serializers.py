from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from .models import Region, City, District, UserProfile, WeatherData
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
    city = CitySerializer()

    class Meta:
        model = UserProfile
        fields = ['gender', 'age', 'city', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    gender = serializers.ChoiceField(choices=UserProfile.GENDER_CHOICES)
    city_name_en = serializers.CharField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'age', 'gender', 'city_name_en', 'first_name', 'last_name')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        user.set_password(validated_data['password'])
        user.save()

        city_name = validated_data.pop('city_name_en')
        try:
            city = City.objects.get(city_name_en=city_name)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({"city_name_en": "City not found."})

        UserProfile.objects.create(
            user=user,
            age=validated_data['age'],
            gender=validated_data['gender'],
            city=city
        )

        return user

class UserProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['gender', 'age', 'city', 'email']

    def update(self, instance, validated_data):
        # Обновляем поля профиля пользователя
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.email = validated_data.get('email', instance.email)

        # Обновляем город, если он указан
        city_name_en = validated_data.get('city_name_en', None)
        if city_name_en:
            try:
                instance.city = City.objects.get(city_name_en=city_name_en)
            except ObjectDoesNotExist:
                raise serializers.ValidationError({"city_name_en": "City not found."})

        instance.save()
        return instance

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'