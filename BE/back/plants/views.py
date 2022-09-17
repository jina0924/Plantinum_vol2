from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import MyplantSerializer, PlantsSerializer, PlantsSearchSerializer, DiarySerializer, MyplantListSerializer
from .models import Myplant, Plants, Diary
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.core.cache import cache


User = get_user_model()


# 전체 식물 조회 => 제공하지 않는 기능, 개발 확인용
@api_view(['GET'])
def plants(request):
    plants = get_list_or_404(Plants)
    serializer = PlantsSerializer(plants, many=True)
    return Response(serializer.data)    


# 내 식물 전체 조회 
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def read_myplant(request, username):
    user = get_object_or_404(User, username=username)
    
    plants = Myplant.objects.filter(user=user).order_by('-pk')

    serializer = MyplantListSerializer(plants, many=True)
    return Response(serializer.data)
    

# 식물 이름 검색
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search(request, plantname):
    plants = Plants.objects.filter(name__contains=plantname)
    serializer = PlantsSearchSerializer(plants, many=True)
    return Response(serializer.data)


# 등록용 식물 검색
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def search_all(request):
    plants = Plants.objects.all()
    serializer = PlantsSearchSerializer(plants, many=True)
    return Response(serializer.data)


from threading import Timer
import random


# 물주기(내 식물) 등록 (등록 전 식물 검색 필요)
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_myplant(request):
    
    user = request.user

    serializer = MyplantSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        plantname = request.data['plantname']

        if Plants.objects.exclude(name='직접 입력하기').filter(name=plantname).exists():
            plant_info = Plants.objects.get(name=plantname)

            serializer.save(user=user, plant_info=plant_info)
        else:
            plant_info = Plants.objects.get(name='직접 입력하기')

            serializer.save(user=user, plant_info=plant_info)

        

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 연결되지 않은 상태, otp도 없는 상태에서 otp 발급
# 1분이 지나면 otp 삭제
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_otp(request, myplant_pk):

    if Myplant.objects.filter(pk=myplant_pk).exists():
        myplant = Myplant.objects.filter(pk=myplant_pk)

        me = request.user.id
        user = myplant.values('user_id')[0]['user_id']
        
        if me == user:  # OTP 요청자와 식물 등록자가 같으면
            if cache.get(f'{me}_{myplant_pk}') == None and myplant.values('is_connected')[0]['is_connected'] == False:  # 해당 식물의 OTP 코드가 발급되지 않았고 연결된 상태가 아니라면

                otp_code = ''

                while otp_code == '':

                    otp_code = random.randint(0, 999999)
                    otp_code = str(otp_code).zfill(6)

                    if Myplant.objects.filter(otp_code=otp_code).exists():  # db 존재 여부 확인
                        otp_code = ''  # 이미 존재하면 재발급

                myplant.update(otp_code=otp_code)

                def set_otp_redis():
                    cache.set(f'{me}_{myplant_pk}', otp_code, timeout=60)  # 지속시간 60초
                set_otp_redis()

                otp_redis = cache.get(f'{me}_{myplant_pk}')

                def delete_otp():
                    myplant.update(otp_code=None)
                Timer(60, delete_otp).start()  # 60초뒤 삭제 함수 실행

                return Response({'otp_code': otp_redis})
            

            elif cache.get(f'{me}_{myplant_pk}') and myplant.values('is_connected')[0]['is_connected'] == False:  # 연결되지 않은 상태로 otp 존재
                otp_redis = cache.get(f'{me}_{myplant_pk}')
                return Response({'otp_code': otp_redis})

            elif myplant.values('is_connected')[0]['is_connected'] == True:  # 해당 식물이 연결된 상태라면
                
                return Response({'detail': '이미 연결되었습니다.'}, status=status.HTTP_400_BAD_REQUEST)

        else:  # OTP 요청자와 식물 등록자가 다르면
            return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)
    else:  # 존재하지 않는 식물pk
        return Response({'detail': '찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)


# otp코드 조회
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def otp_status(request, myplant_pk):
    myplant = get_object_or_404(Myplant, pk=myplant_pk)
    me = request.user.id
    user = myplant.user_id
    
    if me == user:
        is_connected = myplant.is_connected
        if is_connected == True:
            otp_redis = None

        else:
            otp_redis = cache.get(f'{me}_{myplant_pk}')
        print(otp_redis)
        return Response({'otp_code': otp_redis})

    else:
        return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)


# otp 삭제
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def otp_remove(request, myplant_pk):
    myplant = get_object_or_404(Myplant, pk=myplant_pk)
    me = request.user.id
    user = myplant.user_id

    if me == user:
        otp_redis = cache.get(f'{me}_{myplant_pk}')
        if otp_redis:
            cache.delete(f'{me}_{myplant_pk}')
        
            return Response({'otp_code': None})

    else:
        return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)


# 연결끊기
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def disconnect(request, myplant_pk):
    if Myplant.objects.filter(pk=myplant_pk).exists():
        myplant = Myplant.objects.filter(pk=myplant_pk)

        me = request.user.id
        user = myplant.values('user_id')[0]['user_id']

        if me == user:  # 연결끊기 요청자와 식물 등록자가 같으면
            if myplant.values('is_connected')[0]['is_connected'] == True:
                myplant.update(is_connected=False)
                return Response({'is_connected': False})

            else:
                return Response({'detail': '연결상태를 확인해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)
    else:
        return Response({'detail': '찾을 수 없습니다.'}, status=status.HTTP_404_NOT_FOUND)


# 물주기 식물 상세페이지 조회/수정/삭제
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail(request, myplant_pk):
    myplant = get_object_or_404(Myplant, pk=myplant_pk)
    user = myplant.user
    
    def read():
        serializer = MyplantSerializer(myplant)
        return Response(serializer.data)

    def update():

        request_copy_data = request.data.copy()

        if request_copy_data['photo'] == 'same':
            request_copy_data['photo'] = myplant.photo

        if request.user == user:
            serializer = MyplantSerializer(instance=myplant, data=request_copy_data)

            if serializer.is_valid(raise_exception=True):
                if request_copy_data['photo'] != '':

                    serializer.save()

                else:
                
                    photo = 'static/monstera.jpg'
                    serializer.save(photo=photo)

                return Response(serializer.data)

        else:
            return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)

    def delete():
        if request.user == user:
            myplant.delete()
            return Response({'detail': '내식물이 삭제되었습니다.'})

        else:
            return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        return read()
    elif request.method == 'PUT':
        return update()
    elif request.method == 'DELETE':
        return delete()


# 물주기 각 식물 별 다이어리-식물 별 전체조회/다이어리 작성
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def diary(request, myplant_pk):

    def read_diary():
        diary = Diary.objects.filter(my_plant_id=myplant_pk).order_by('-pk')
        serializer = DiarySerializer(diary, many=True)
        return Response(serializer.data)

    def create_diary():
        my_plant = get_object_or_404(Myplant, pk=myplant_pk)
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(my_plant=my_plant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'GET':
        return read_diary()
    elif request.method == 'POST':
        return create_diary()