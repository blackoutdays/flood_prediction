from rest_framework import generics
from .models import Region, City, District, UserProfile
from .serializers import RegionSerializer, CitySerializer, DistrictSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema

# Регион CRUD
class RegionListCreateView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @swagger_auto_schema(
        operation_description="Получение списка всех регионов",
        responses={200: RegionSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение списка всех регионов
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создание нового региона",
        request_body=RegionSerializer,
        responses={201: RegionSerializer}
    )
    def post(self, request, *args, **kwargs):
        """
        POST: Создание нового региона
        """
        return super().post(request, *args, **kwargs)

class RegionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    @swagger_auto_schema(
        operation_description="Получение конкретного региона по ID",
        responses={200: RegionSerializer}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение региона по ID
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновление информации о регионе",
        request_body=RegionSerializer,
        responses={200: RegionSerializer}
    )
    def put(self, request, *args, **kwargs):
        """
        PUT: Полное обновление информации о регионе
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о регионе",
        request_body=RegionSerializer,
        responses={200: RegionSerializer}
    )
    def patch(self, request, *args, **kwargs):
        """
        PATCH: Частичное обновление информации о регионе
        """
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление региона по ID",
        responses={204: 'Регион успешно удален'}
    )
    def delete(self, request, *args, **kwargs):
        """
        DELETE: Удаление региона по ID
        """
        return super().delete(request, *args, **kwargs)

# Город CRUD
class CityListCreateView(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @swagger_auto_schema(
        operation_description="Получение списка всех городов",
        responses={200: CitySerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение списка всех городов
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создание нового города",
        request_body=CitySerializer,
        responses={201: CitySerializer}
    )
    def post(self, request, *args, **kwargs):
        """
        POST: Создание нового города
        """
        return super().post(request, *args, **kwargs)

class CityRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @swagger_auto_schema(
        operation_description="Получение города по ID",
        responses={200: CitySerializer}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение города по ID
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновление информации о городе",
        request_body=CitySerializer,
        responses={200: CitySerializer}
    )
    def put(self, request, *args, **kwargs):
        """
        PUT: Полное обновление информации о городе
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о городе",
        request_body=CitySerializer,
        responses={200: CitySerializer}
    )
    def patch(self, request, *args, **kwargs):
        """
        PATCH: Частичное обновление информации о городе
        """
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление города по ID",
        responses={204: 'Город успешно удален'}
    )
    def delete(self, request, *args, **kwargs):
        """
        DELETE: Удаление города по ID
        """
        return super().delete(request, *args, **kwargs)

# Район CRUD
class DistrictListCreateView(generics.ListCreateAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    @swagger_auto_schema(
        operation_description="Получение списка всех районов",
        responses={200: DistrictSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение списка всех районов
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Создание нового района",
        request_body=DistrictSerializer,
        responses={201: DistrictSerializer}
    )
    def post(self, request, *args, **kwargs):
        """
        POST: Создание нового района
        """
        return super().post(request, *args, **kwargs)

class DistrictRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    @swagger_auto_schema(
        operation_description="Получение района по ID",
        responses={200: DistrictSerializer}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение района по ID
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновление информации о районе",
        request_body=DistrictSerializer,
        responses={200: DistrictSerializer}
    )
    def put(self, request, *args, **kwargs):
        """
        PUT: Полное обновление информации о районе
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление информации о районе",
        request_body=DistrictSerializer,
        responses={200: DistrictSerializer}
    )
    def patch(self, request, *args, **kwargs):
        """
        PATCH: Частичное обновление информации о районе
        """
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Удаление района по ID",
        responses={204: 'Район успешно удален'}
    )
    def delete(self, request, *args, **kwargs):
        """
        DELETE: Удаление района по ID
        """
        return super().delete(request, *args, **kwargs)

# Профиль пользователя CRUD
class UserProfileView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Получение профиля пользователя",
        responses={200: UserProfileSerializer}
    )
    def get(self, request, *args, **kwargs):
        """
        GET: Получение профиля пользователя
        """
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Обновление профиля пользователя",
        request_body=UserProfileSerializer,
        responses={200: UserProfileSerializer}
    )
    def put(self, request, *args, **kwargs):
        """
        PUT: Полное обновление профиля пользователя
        """
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Частичное обновление профиля пользователя",
        request_body=UserProfileSerializer,
        responses={200: UserProfileSerializer}
    )
    def patch(self, request, *args, **kwargs):
        """
        PATCH: Частичное обновление профиля пользователя
        """
        return super().patch(request, *args, **kwargs)