from rest_framework import serializers
from .models import Juso, Leaf82
from django.contrib.auth import get_user_model


User = get_user_model()


class JusoSidoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juso
        fields = ('pk', 'sido',)


class JusoSigunguSerializer(serializers.ModelSerializer):

    class Meta:
        model = Juso
        fields = ('pk', 'sigungu',)


class Leaf82Serializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username', 'nickname', 'photo',)

    user = UserSerializer(read_only=True)

    class JusoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Juso
            fields = '__all__'

    addr = JusoSerializer(read_only=True)

    class Meta:
        model = Leaf82
        fields = '__all__'
        read_only_fields = ('posting_addr',)


class Leaf82ListSerializer(serializers.ModelSerializer):

    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('pk', 'username',)

    user = UserSerializer(read_only=True)

    class JusoSerializer(serializers.ModelSerializer):
        class Meta:
            model = Juso
            fields = '__all__'

    addr = JusoSerializer(read_only=True)

    class Meta:
        model = Leaf82
        fields = ('pk', 'plantname', 'photo', 'price', 'category_class', 'status_class', 'addr', 'posting_addr', 'user',)
        read_only_fields = ('posting_addr',)
