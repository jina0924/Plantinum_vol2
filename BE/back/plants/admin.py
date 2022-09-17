from django.contrib import admin
from .models import Plants, Myplant, Sensing, Diary

# Register your models here.
admin.site.register(Plants)
admin.site.register(Myplant)
admin.site.register(Sensing)
admin.site.register(Diary)