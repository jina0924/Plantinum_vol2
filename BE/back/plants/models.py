from django.db import models
from django.conf import settings
from .validators import plants_validator, watering_validator, moisture_validator


class Plants(models.Model):
    name = models.CharField(max_length=20)
    watercycle_spring = models.CharField(validators = [plants_validator], max_length=6)
    watercycle_spring_nm = models.CharField(max_length=30)
    watercycle_summer = models.CharField(validators = [plants_validator], max_length=6)
    watercycle_summer_nm = models.CharField(max_length=30)
    watercycle_autumn = models.CharField(validators = [plants_validator], max_length=6)
    watercycle_autumn_nm = models.CharField(max_length=30)
    watercycle_winter = models.CharField(validators = [plants_validator], max_length=6)
    watercycle_winter_nm = models.CharField(max_length=30)
    specl_manage_info = models.TextField(blank=True)


class Myplant(models.Model):
    nickname = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    otp_code = models.CharField(max_length=6, unique=True, null=True)
    plant_info = models.ForeignKey(Plants, on_delete=models.PROTECT)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='images/myplant/', default='static/monstera.jpg')
    is_connected = models.BooleanField(default=False)
    tmp = models.CharField(max_length=20, blank=True)


from annoying.fields import AutoOneToOneField


class Sensing(models.Model):
    remaining_water = models.BooleanField(default=False)
    state_led = models.BooleanField(default=False)
    moisture_level = models.IntegerField(validators = [moisture_validator], default=0)
    last_watering = models.CharField(validators = [watering_validator], max_length=16, blank=True)
    # my_plant = models.OneToOneField(Myplant, on_delete=models.CASCADE)
    my_plant = AutoOneToOneField(Myplant, on_delete=models.CASCADE)


class Diary(models.Model):
    content = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='images/diary/', default='static/monstera.jpg')
    diary_created_at = models.DateTimeField(auto_now_add=True)
    public_private = models.BooleanField(default=False)
    my_plant = models.ForeignKey(Myplant, on_delete=models.CASCADE)
