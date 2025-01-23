from django.http import JsonResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
import logging
from .models import Region, City, District, UserProfile, Notification, WeatherData
from .serializers import RegionSerializer, CitySerializer, DistrictSerializer, UserProfileSerializer, \
    UserRegistrationSerializer, WeatherDataSerializer
from django.contrib.auth.models import User
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import folium
from django.http import HttpResponse
from django.shortcuts import render
import os
from django.conf import settings
import requests
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.renderers import JSONRenderer
from django.core.mail import EmailMessage
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.password_validation import validate_password

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




# ------------------- User Registration -------------------
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
            # Проверка на существование пользователя
            if User.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

            # Создание пользователя
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                first_name=serializer.validated_data.get('first_name', ''),
                last_name=serializer.validated_data.get('last_name', '')
            )

            # Проверка существования города
            city_name = serializer.validated_data['city_name_en']
            try:
                city = City.objects.get(city_name_en=city_name)
            except City.DoesNotExist:
                return Response({"city_name_en": "City not found."}, status=status.HTTP_400_BAD_REQUEST)

            # Создание профиля пользователя
            UserProfile.objects.create(
                user=user,
                age=serializer.validated_data['age'],
                gender=serializer.validated_data['gender'],
                city=city,
                email=user.email
            )

            # Отправка email
            subject = "Welcome to the System"
            template_name = "emails/email_template.html"
            context = {
                "first_name": user.first_name,
                "username": user.username,
                "email": user.email,
                "city": city_name
            }
            email_sent = send_email_notification(subject, template_name, context, user.email)
            if not email_sent:
                logger.error("Email notification failed for user: %s", user.username)

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


# ------------------- User Login -------------------
class UserLoginView(APIView):
    """
    Аутентификация пользователя по username и паролю.
    """
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Username и пароль обязательны'}, status=status.HTTP_400_BAD_REQUEST)

        # Аутентификация пользователя
        user = authenticate(username=username, password=password)

        if user:
            # Генерация JWT токенов
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'username': user.username,
            }, status=status.HTTP_200_OK)

        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)


# ------------------- Utility Functions -------------------
def create_notification(user, message):
    """Создает уведомление для пользователя и отправляет email."""
    try:
        notification = Notification.objects.create(user=user, message=message)
        notification.send_email()
    except Exception as e:
        logger.error(f"Error creating notification for user {user.username}: {e}")


def send_email_notification(subject, template_name, context, to_email):
    """Отправка email уведомления с использованием HTML шаблона."""
    try:
        html_message = render_to_string(template_name, context)
        email = EmailMessage(
            subject,
            html_message,
            settings.DEFAULT_FROM_EMAIL,
            [to_email]
        )
        email.content_subtype = "html"
        email.send()
        logger.info(f"Email sent successfully to {to_email}")
        print(f"Email sent successfully to {to_email}")  # Для отладки
        return True
    except Exception as e:
        logger.error(f"Error sending email to {to_email}: {e}")
        print(f"Error sending email to {to_email}: {e}")  # Для отладки
        return False

class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        old_password = request.data.get('old_password')
        new_password = request.data.get('new_password')

        if not user.check_password(old_password):
            return Response({'error': 'Incorrect old password'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            validate_password(new_password, user)
            user.set_password(new_password)
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        # class UserLoginView(APIView):
        #     renderer_classes = [JSONRenderer]
        #
        #     def post(self, request, *args, **kwargs):
        #         username = request.data.get('username')
        #         password = request.data.get('password')
        #         user = authenticate(request, username=username, password=password)
        #
        #         if user:
        #             refresh = RefreshToken.for_user(user)
        #             return Response({
        #                 'refresh': str(refresh),
        #                 'access': str(refresh.access_token),
        #                 'username': user.username,
        #             }, status=status.HTTP_200_OK)
        #
        #         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        #

class WeatherDataAPIView(APIView):
    @swagger_auto_schema(
        operation_description="Retrieve all weather data",
        responses={
            200: WeatherDataSerializer(many=True),
            400: "Bad Request",
        },
    )
    def get(self, request):
        weather_data = WeatherData.objects.all()
        serializer = WeatherDataSerializer(weather_data, many=True)
        return Response(serializer.data)