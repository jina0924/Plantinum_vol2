from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
import random
from leaf82.models import Leaf82

from django.contrib.auth import get_user_model
User = get_user_model()


class CustomRegisterSerializer(RegisterSerializer):

    # phone_number = serializers.CharField(max_length=11)
    # addr = serializers.CharField(max_length=100)
    # zip_code = serializers.CharField(max_length=5)
    # nickname = serializers.CharField(max_length=15)
    email = serializers.EmailField()

    def get_cleaned_data(self):
        full_nickname = ''

        while full_nickname == '':
            nick1_lst = ['촉촉한', '싱싱한', '늘푸른', '건강한', '새내기']
            nick2_lst = ['참나무', '소나무', '올리브나무', '야자나무', '귤나무']
            nick1 = random.choice(nick1_lst)
            nick2 = random.choice(nick2_lst)
            nick3 = str(random.randint(0, 9999))
        
            full_nickname = nick1+nick2+nick3
            if User.objects.filter(nickname=full_nickname).exists():
                full_nickname = ''

        data = super().get_cleaned_data()
        # data['phone_number'] = self._validated_data.get('phone_number', '')
        # data['addr'] = self._validated_data.get('addr', '')
        # data['zip_code'] = self._validated_data.get('zip_code', '')
        data['nickname'] = self._validated_data.get('nickname', full_nickname)
        data['email'] = self._validated_data.get('email', '')
        return data


class MyProfileSerializer(serializers.ModelSerializer):

    myplant_count = serializers.IntegerField(source='myplant_set.count', read_only=True)

    class Leaf82Serializer(serializers.ModelSerializer):

        class Meta:

            model = Leaf82
            fields = ('pk', 'photo', 'posting_addr', 'plantname',)

    leaf82_set = Leaf82Serializer(many=True, read_only=True)

    class Meta:

        model = User
        fields = ('pk', 'nickname', 'email', 'phone_number', 'addr', 'zip_code', 'myplant_count', 'photo', 'leaf82_set',)


class UpdateUserInformationSerializer(serializers.ModelSerializer):

    myplant_count = serializers.IntegerField(source='myplant_set.count', read_only=True)
    dday = serializers.IntegerField(read_only=True)

    class Meta:

        model = User
        fields = ('pk', 'nickname', 'email', 'phone_number', 'addr', 'zip_code', 'myplant_count', 'dday', 'photo',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User
        fields = ('pk', 'nickname', 'photo', 'username',)

