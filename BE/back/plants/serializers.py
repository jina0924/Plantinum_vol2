from rest_framework import serializers
from .models import Plants, Myplant, Sensing, Diary
from django.contrib.auth import get_user_model

User = get_user_model()


class DiarySerializer(serializers.ModelSerializer):

    class MyplantSerializer(serializers.ModelSerializer):

        class Meta:
            model = Myplant
            fields = ('pk', 'nickname',)
    
    my_plant = MyplantSerializer(read_only=True)

    class Meta:

        model = Diary
        fields = '__all__'


class MyplantSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname',)

    user = UserSerializer(read_only=True)

    class PlantsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Plants
            fields = ('pk', 'name', 'watercycle_spring_nm', 'watercycle_summer_nm', 'watercycle_autumn_nm', 'watercycle_winter_nm', 'specl_manage_info',)

    plant_info = PlantsSerializer(read_only=True)
    plantname = serializers.CharField(read_only=True)

    is_connected = serializers.BooleanField(read_only=True)

    class SensingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Sensing
            fields = '__all__'
    
    sensing = SensingSerializer(read_only=True)

    diary_set = DiarySerializer(many=True, read_only=True)
    diary_count = serializers.IntegerField(source='diary_set.count', read_only=True)
    
    class Meta:
        model = Myplant
        fields = '__all__'


class MyplantListSerializer(serializers.ModelSerializer):

    class SensingSerializer(serializers.ModelSerializer):
        class Meta:
            model = Sensing
            fields = ('moisture_level',)
    
    sensing = SensingSerializer(read_only=True)

    diary_count = serializers.IntegerField(source='diary_set.count', read_only=True)
    
    class Meta:
        model = Myplant
        fields = ('pk', 'nickname', 'photo', 'sensing', 'diary_count', 'is_connected',)


class PlantsSerializer(serializers.ModelSerializer):

    class MyplantSerializer(serializers.ModelSerializer):
        class Meta:
            model = Myplant
            fields = ('pk', 'nickname',)
        
    myplant_set = MyplantSerializer(many=True, read_only=True)

    class Meta:
        model = Plants
        fields = '__all__'


class PlantsSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plants
        fields = ('pk', 'name',)


class SensingSerializer(serializers.ModelSerializer):

    class MyplantSerializer(serializers.ModelSerializer):
        
        class Meta:
            model = Myplant
            fields = ('pk', 'nickname',)

    my_plant = MyplantSerializer(read_only=True)

    class Meta:
        model = Sensing
        fields = '__all__'