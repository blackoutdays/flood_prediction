from django.contrib import admin
from .models import Region, City, District, UserProfile

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name_en', 'region_name_ru', 'region_name_kk')
    search_fields = ('region_name_en', 'region_name_ru', 'region_name_kk')  # Поля для поиска
    list_filter = ('region_name_en', 'region_name_ru')  # Фильтрация по названиям регионов

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name_en', 'city_name_ru', 'city_name_kk', 'population', 'area', 'region')
    search_fields = ('city_name_en', 'city_name_ru', 'city_name_kk')  # Поля для поиска
    list_filter = ('region', 'population')  # Фильтрация по региону и населению

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name_en', 'district_name_ru', 'district_name_kk', 'population', 'area', 'city')
    search_fields = ('district_name_en', 'district_name_ru', 'district_name_kk')  # Поля для поиска
    list_filter = ('city', 'population')  # Фильтрация по городу и населению

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'gender', 'age', 'city')
    search_fields = ('user__username', 'city__city_name_en')  # Поля для поиска по пользователю и городу
    list_filter = ('gender', 'city')  # Фильтрация по полу и городу