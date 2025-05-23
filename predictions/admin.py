from django.contrib import admin
from .models import Region, City, District, UserProfile, WeatherData

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('region_name_en', 'region_name_ru', 'region_name_kk')
    search_fields = ('region_name_en', 'region_name_ru', 'region_name_kk')
    list_filter = ('region_name_en', 'region_name_ru')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('city_name_en', 'city_name_ru', 'city_name_kk', 'population', 'area', 'region')
    search_fields = ('city_name_en', 'city_name_ru', 'city_name_kk')
    list_filter = ('region', 'population')

@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('district_name_en', 'district_name_ru', 'district_name_kk', 'population', 'area', 'city')
    search_fields = ('district_name_en', 'district_name_ru', 'district_name_kk')
    list_filter = ('city', 'population')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'gender', 'age', 'city', 'email')
    search_fields = ('user', 'first_name', 'last_name', 'gender', 'age', 'city', 'email')
    list_filter = ('gender', 'city')

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = (
        "date", "air_temp_avg", "air_temp_max", "air_temp_min",
        "soil_temp_avg", "soil_temp_max", "soil_temp_min",
        "flood_risk", "flood_risk_week", "flood_risk_month"
    )
    search_fields = ("date", "air_temp_avg", "flood_risk")
    list_filter = ("date", "flood_risk_month", "flood_risk_week")

admin.site.register(UserProfile, UserProfileAdmin)

