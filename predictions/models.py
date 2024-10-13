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