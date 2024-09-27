from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.urls import path, include
from .views import RegionListCreateView, RegionRetrieveUpdateDestroyView, CityListCreateView, CityRetrieveUpdateDestroyView, DistrictListCreateView, DistrictRetrieveUpdateDestroyView, UserProfileView

schema_view = get_schema_view(
   openapi.Info(
      title="Flood Prediction API",
      default_version='v1',
      description="API for managing regions, cities, districts, and user profiles",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@local.api"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger-документация
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    # Эндпоинты для регионов
    path('regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('regions/<int:pk>/', RegionRetrieveUpdateDestroyView.as_view(), name='region-detail'),

    # Эндпоинты для городов
    path('cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('cities/<int:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),

    # Эндпоинты для районов
    path('districts/', DistrictListCreateView.as_view(), name='district-list-create'),
    path('districts/<int:pk>/', DistrictRetrieveUpdateDestroyView.as_view(), name='district-detail'),

    # Эндпоинт для профиля пользователя
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]