from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import MyProfileSerializer, UpdateUserInformationSerializer, UserSerializer
import datetime
from rest_framework import status


User = get_user_model()


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    serializer = MyProfileSerializer(user)
    
    pk = user.pk
    nickname = user.nickname
    email = user.email
    phone_number = user.phone_number
    addr = user.addr
    zip_code = user.zip_code
    myplant_count = serializer.data.get('myplant_count')
    date_joined = user.date_joined
    today = datetime.datetime.now()
    dday = (today - date_joined).days+1
    img_juso = 'https://plantinum.s3.ap-northeast-2.amazonaws.com/' + str(user.photo)
    photo = img_juso
    leaf82_set = serializer.data.get('leaf82_set')

    data = {
        'pk': pk,
        'nickname': nickname,
        'email': email,
        'phone_number': phone_number,
        'addr': addr,
        'zip_code': zip_code,
        'myplant_count': myplant_count,
        'dday': dday,
        'photo': photo,
        'leaf82_set': leaf82_set
    }
    
    return Response(data)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def currentuser(request):
    user = request.user
    serializer = UserSerializer(user)

    return Response(serializer.data)


@api_view(['PUT'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def updateuserinformation(request):
    user = request.user
    myplant_count = UpdateUserInformationSerializer(user).data.get('myplant_count')

    request_copy_data = request.data.copy()

    if request_copy_data['photo'] == 'same':
        request_copy_data['photo'] = user.photo

    serializer = UpdateUserInformationSerializer(instance=user, data=request_copy_data)
    date_joined = user.date_joined
    today = datetime.datetime.now()
    dday = (today - date_joined).days+1
    
    new_email = request.data['email']
    new_nickname = request.data['nickname']

    if User.objects.filter(email=new_email).exists():
        email_user = User.objects.filter(email=new_email)[0]
    if User.objects.filter(nickname=new_nickname).exists():
        nickname_user = User.objects.filter(nickname=new_nickname)[0]


    # 이메일과 닉네임 모두 이미 존재하는 경우
    if User.objects.filter(email=new_email).exists() and User.objects.filter(nickname=new_nickname).exists():

        # 이메일과 닉네임 모두 유저의 기존 값과 다른 경우
        if email_user != user and nickname_user != user:
            return Response({
                'email': '이메일이 이미 존재합니다.',
                'nickname': '닉네임이 이미 존재합니다.'
                }, status=status.HTTP_409_CONFLICT)

        # 이메일은 유저의 기존 값과 동일, 닉네임은 유저의 기존 값과 다른 경우
        if email_user == user and nickname_user != user:
            return Response({
            'nickname': '닉네임이 이미 존재합니다.'
            }, status=status.HTTP_409_CONFLICT)

        # 이메일은 유저의 기존 값과 다르고, 닉네임은 유저의 기존 값과 동일한 경우
        if email_user != user and nickname_user == user:
            return Response({
            'email': '이메일이 이미 존재합니다.',
            }, status=status.HTTP_409_CONFLICT)

        # 이메일과 닉네임 모두 유저의 기존 값과 같은 경우 - 그대로 저장
        if email_user == user and nickname_user == user:
            if serializer.is_valid(raise_exception=True):

                if request_copy_data['photo'] != '':
                    serializer.save(myplant_count=myplant_count, dday=dday)

                else:
                    photo = 'static/profile.jpg'
                    serializer.save(myplant_count=myplant_count, dday=dday, photo=photo)

                return Response(serializer.data)

    # 이메일이 이미 존재하는 경우
    if User.objects.filter(email=new_email).exists():

        # 이메일이 유저의 기존 값과 다른 경우
        if email_user != user:
            return Response({
                'email': '이메일이 이미 존재합니다.',
                }, status=status.HTTP_409_CONFLICT)

        # 이메일이 유저의 기존 값과 같은 경우
        if email_user == user:
            if serializer.is_valid(raise_exception=True):
                if request_copy_data['photo'] != '':
                    serializer.save(myplant_count=myplant_count, dday=dday)

                else:
                    photo = 'static/profile.jpg'
                    serializer.save(myplant_count=myplant_count, dday=dday, photo=photo)
                
                return Response(serializer.data)

    # 닉네임이 이미 존재하는 경우
    if User.objects.filter(nickname=request.data['nickname']).exists():

        # 닉네임이 유저의 기존 값과 다른 경우
        if nickname_user != user:
            return Response({
                'nickname': '닉네임이 이미 존재합니다.'
                }, status=status.HTTP_409_CONFLICT)

        # 닉네임이 유저의 기존 값과 같은 경우
        if nickname_user == user:
            if serializer.is_valid(raise_exception=True):
                if request_copy_data['photo'] != '':
                    serializer.save(myplant_count=myplant_count, dday=dday)

                else:
                    photo = 'static/profile.jpg'
                    serializer.save(myplant_count=myplant_count, dday=dday, photo=photo)
                return Response(serializer.data)

    # 그 외 유효성검사에 걸리는 경우
    if serializer.is_valid(raise_exception=True):

        if request_copy_data['photo'] != '':
            serializer.save(myplant_count=myplant_count, dday=dday)

        else:
            photo = 'static/profile.jpg'
            serializer.save(myplant_count=myplant_count, dday=dday, photo=photo)
    
        return Response(serializer.data)


@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def withdraw(request):
    user = User.objects.get(username=request.user)
    user.delete()
    return Response({'detail': '정상적으로 탈퇴되었습니다.'})

