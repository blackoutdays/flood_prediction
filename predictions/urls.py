from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.http import HttpResponseRedirect
from .views import RegionListCreateView, RegionRetrieveUpdateDestroyView, CityListCreateView, CityRetrieveUpdateDestroyView, DistrictListCreateView, DistrictRetrieveUpdateDestroyView, UserProfileView

schema_view = get_schema_view(
    openapi.Info(
        title="Flood Prediction API",
        default_version='v1',
        description="API для управления регионами, городами, районами и профилями пользователей",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@local.api"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Перенаправление на Swagger по умолчанию при обращении к корню
    path('', lambda request: HttpResponseRedirect('swagger/')),

    # Swagger и Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),  # Redoc UI

    # Админка
    path('admin/', admin.site.urls),  # Панель администратора

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