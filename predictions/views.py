from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
import logging
from .models import Region, City, District, UserProfile
from .serializers import RegionSerializer, CitySerializer, DistrictSerializer, UserProfileSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

def home(request):
    return JsonResponse({"message": "Welcome to the test_microservice Service API!"})

# Region CRUD Views
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of regions",
        responses={200: RegionSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new region",
        request_body=RegionSerializer,
        responses={201: RegionSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class RegionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a region by ID",
        responses={200: RegionSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a region",
        request_body=RegionSerializer,
        responses={200: RegionSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a region",
        responses={204: 'Region successfully deleted'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# City CRUD Views
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of cities",
        responses={200: CitySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new city",
        request_body=CitySerializer,
        responses={201: CitySerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @swagger_auto_schema(
        operation_description="Retrieve a city by ID",
        responses={200: CitySerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a city",
        request_body=CitySerializer,
        responses={200: CitySerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a city",
        responses={204: 'City successfully deleted'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# District CRUD Views
class DistrictListCreateView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of districts",
        responses={200: DistrictSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new district",
        request_body=DistrictSerializer,
        responses={201: DistrictSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class DistrictRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a district by ID",
        responses={200: DistrictSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a district",
        request_body=DistrictSerializer,
        responses={200: DistrictSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a district",
        responses={204: 'District successfully deleted'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)









# User Profile CRUD Views
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retrieve a user profile",
        responses={200: UserProfileSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a user profile",
        request_body=UserProfileSerializer,
        responses={200: UserProfileSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Partially update a user profile",
        request_body=UserProfileSerializer,
        responses={200: UserProfileSerializer}
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @swagger_auto_schema(
        operation_description="Create a new user profile",
        request_body=UserProfileSerializer,
        responses={201: UserProfileSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserProfileRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    @swagger_auto_schema(
        operation_description="Retrieve a user profile by ID",
        responses={200: UserProfileSerializer}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Update a user profile",
        request_body=UserProfileSerializer,
        responses={200: UserProfileSerializer}
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Delete a user profile",
        responses={204: 'User profile successfully deleted'}
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


class CityListView(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @swagger_auto_schema(
        operation_description="Retrieve a list of cities",
        responses={200: CitySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

    @swagger_auto_schema(
        operation_description="User registration",
        request_body=UserRegistrationSerializer,
        responses={201: UserRegistrationSerializer}
    )
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Creating a user with first_name and last_name
            user = User(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                first_name=serializer.validated_data.get('first_name', ''),  # Optional
                last_name=serializer.validated_data.get('last_name', ''),    # Optional
            )
            user.set_password(serializer.validated_data['password'])
            user.save()

            city_name = serializer.validated_data['city_name_en']
            try:
                city = City.objects.get(city_name_en=city_name)
            except City.DoesNotExist:
                return Response({"city_name_en": "City not found."}, status=status.HTTP_400_BAD_REQUEST)

            UserProfile.objects.create(
                user=user,
                age=serializer.validated_data['age'],
                gender=serializer.validated_data['gender'],
                city=city,
                email=user.email
            )

            return Response({
                "user": {
                    "username": user.username,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "age": serializer.validated_data['age'],
                    "gender": serializer.validated_data['gender'],
                    "city": city_name
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)