from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Juso(models.Model):
    sido = models.CharField(max_length=20)
    sigungu = models.CharField(max_length=20)


class Leaf82(models.Model):
    CATEGORY_CHOICES = (
        ('분양해요', '분양해요'),
        ('분양받아요', '분양받아요')
    )
    STATUS_CHOICES = (
        ('분양대기', '분양대기'),
        ('분양완료', '분양완료'),
        ('분양예약', '분양예약')
    )

    plantname = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images/leaf82/', default='static/monstera.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.CharField(max_length=1000)
    price = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10000000)])
    category_class = models.CharField(max_length=5, choices=CATEGORY_CHOICES, default='분양해요')
    status_class = models.CharField(max_length=4, choices=STATUS_CHOICES, default='분양대기')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    addr = models.ForeignKey(Juso, on_delete=models.PROTECT)
    posting_addr = models.IntegerField(default=0)