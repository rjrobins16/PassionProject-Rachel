from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.gis.geos import Point
# Create your models here.

class Profile(models.Model):
    current_user = models.OneToOneField(User, on_delete=models.CASCADE,
    primary_key=True)
    is_user = models.BooleanField(default = True)
    is_stylist = models.BooleanField(default=False)
    location = models.PointField =
    TypeofStylist = models.CharField(max_length = 100, null=True, blank=True)
    DateOfBirth = models.DateTimeField(null=True)
    Profile_Picture = models.ImageField(upload_to='media', null=True, blank=True)


class UserImages(models.Model):
    Date_Time = models.DateTimeField(auto_now_add = True)
    Author = models.ForeignKey(User, on_delete = models.CASCADE)








