from django.http import JsonResponse
from rest_framework import generics
from .models import Region, City, District, UserProfile
from .serializers import RegionSerializer, CitySerializer, DistrictSerializer, UserProfileSerializer, UserRegistrationSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
import logging

logger = logging.getLogger(__name__)

def home(request):
    return JsonResponse({"message": "Welcome to the test_microservice Service API!"})
from rest_framework import generics
from .models import Region, City, District, UserProfile
from .serializers import RegionSerializer, CitySerializer, DistrictSerializer, UserProfileSerializer

# Region CRUD Views
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

class RegionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

# City CRUD Views
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

# District CRUD Views
class DistrictListCreateView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class DistrictRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

# User Profile CRUD Views
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileCreateView(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

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
    permission_classes = [IsAuthenticated]  # Only authenticated users can access this view

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