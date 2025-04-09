from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    region_name_en = models.CharField(max_length=255, verbose_name="Region Name (English)")
    region_name_ru = models.CharField(max_length=255, verbose_name="Region Name (Russian)")
    region_name_kk = models.CharField(max_length=255, verbose_name="Region Name (Kazakh)")
    population = models.IntegerField(verbose_name="Population")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Area in sq.km")
    capital_name_en = models.CharField(max_length=255, verbose_name="Capital Name (English)")
    capital_name_ru = models.CharField(max_length=255, verbose_name="Capital Name (Russian)")
    capital_name_kk = models.CharField(max_length=255, verbose_name="Capital Name (Kazakh)")
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Longitude")

    def __str__(self):
        return self.region_name_en

    class Meta:
        verbose_name = 'Region'
        verbose_name_plural = 'Regions'

class City(models.Model):
    id_city = models.AutoField(primary_key=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='cities', verbose_name="Region", db_column='id_region')
    city_name_en = models.CharField(max_length=255, verbose_name="City Name (English)")
    city_name_ru = models.CharField(max_length=255, verbose_name="City Name (Russian)")
    city_name_kk = models.CharField(max_length=255, verbose_name="City Name (Kazakh)")
    population = models.IntegerField(verbose_name="Population")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Area in sq.km", default=0.0)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=10, decimal_places=7, verbose_name="Longitude")

    def __str__(self):
        return self.city_name_en

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'

class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts', verbose_name="City")
    district_name_en = models.CharField(max_length=255, verbose_name="District Name (English)")
    district_name_ru = models.CharField(max_length=255, verbose_name="District Name (Russian)")
    district_name_kk = models.CharField(max_length=255, verbose_name="District Name (Kazakh)")
    population = models.IntegerField(verbose_name="Population")
    area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Area in sq.km")

    def __str__(self):
        return self.district_name_en

    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'


class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('P', 'Prefer not to say'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', verbose_name="User")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="Gender")
    age = models.PositiveIntegerField(verbose_name="Age")
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="City")
    email = models.EmailField(null=True, blank=True, verbose_name="Email")  # Ensure this is correctly defined

    def __str__(self):
        return f"{self.user.username} - {self.city}"

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user} - {self.message}"

    def send_email(self):
        # Send email notification
        send_mail(
            subject='New Notification',
            message=self.message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

class WeatherData(models.Model):
    air_temp_avg = models.FloatField(verbose_name="Средняя температура воздуха")
    air_temp_max = models.FloatField(verbose_name="Максимальная температура воздуха")
    air_temp_min = models.FloatField(verbose_name="Минимальная температура воздуха")
    soil_temp_avg = models.FloatField(verbose_name="Средняя температура почвы")
    soil_temp_max = models.FloatField(verbose_name="Максимальная температура почвы")
    soil_temp_min = models.FloatField(verbose_name="Минимальная температура почвы")
    dew_point_min = models.FloatField(verbose_name="Минимальная точка росы")
    vapor_pressure_avg = models.FloatField(verbose_name="Среднее парциальное давление")
    humidity_avg = models.FloatField(verbose_name="Средняя влажность")
    humidity_min = models.FloatField(verbose_name="Минимальная влажность")
    saturation_deficit_avg = models.FloatField(verbose_name="Средний дефицит насыщения")
    saturation_deficit_max = models.FloatField(verbose_name="Максимальный дефицит насыщения")
    pressure_station = models.FloatField(verbose_name="Давление на уровне станции")
    pressure_sea = models.FloatField(verbose_name="Давление на уровне моря")
    cloud_total = models.FloatField(verbose_name="Общая облачность")
    cloud_lower = models.FloatField(verbose_name="Нижняя облачность")
    wind_speed_avg = models.FloatField(verbose_name="Средняя скорость ветра")
    wind_speed_max = models.FloatField(verbose_name="Максимальная скорость ветра")
    wind_speed_abs_max = models.FloatField(verbose_name="Абсолютная максимальная скорость ветра")
    precipitation = models.FloatField(verbose_name="Количество осадков")
    soil_condition_code = models.IntegerField(verbose_name="Код состояния почвы")
    snow_cover_state = models.IntegerField(verbose_name="Состояние снежного покрова")
    snow_cover_height_cm = models.FloatField(verbose_name="Высота снежного покрова, см")
    date = models.DateTimeField(verbose_name="Дата")
    flood_risk = models.FloatField(verbose_name="Риск паводков")
    week = models.IntegerField(verbose_name="Неделя")
    flood_risk_week = models.FloatField(verbose_name="Риск паводков (неделя)")
    month = models.IntegerField(verbose_name="Месяц")
    flood_risk_month = models.FloatField(verbose_name="Риск паводков (месяц)")

    def __str__(self):
        return f"Weather Data ({self.date})"

    class Meta:
        managed = False
        db_table = 'placeholder'
        verbose_name = "AI flood"
        verbose_name_plural = "AI flood prediction"