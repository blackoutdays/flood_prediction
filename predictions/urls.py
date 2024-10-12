from django.urls import path, include
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    RegionListCreateView,
    RegionRetrieveUpdateDestroyView,
    CityListCreateView,
    CityRetrieveUpdateDestroyView,
    DistrictListCreateView,
    DistrictRetrieveUpdateDestroyView,
    UserProfileView,
    UserProfileCreateView,
    UserProfileRetrieveUpdateView,
    UserRegistrationView,
)

# Swagger schema view configuration
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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('admin/', admin.site.urls),
    path('register/', UserRegistrationView.as_view(), name='user-registry'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/regions/', RegionListCreateView.as_view(), name='region-list-create'),
    path('api/regions/<int:pk>/', RegionRetrieveUpdateDestroyView.as_view(), name='region-detail'),
    path('api/cities/', CityListCreateView.as_view(), name='city-list-create'),
    path('api/cities/<int:pk>/', CityRetrieveUpdateDestroyView.as_view(), name='city-detail'),
    path('api/districts/', DistrictListCreateView.as_view(), name='district-list-create'),
    path('api/districts/<int:pk>/', DistrictRetrieveUpdateDestroyView.as_view(), name='district-detail'),
    path('api/user-profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/user-profile/create/', UserProfileCreateView.as_view(), name='user-profile-create'),
    path('api/user-profile/<int:pk>/', UserProfileRetrieveUpdateView.as_view(), name='user-profile-detail'),
]