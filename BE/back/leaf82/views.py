from django.shortcuts import get_object_or_404
from .serializers import JusoSidoSerializer, JusoSigunguSerializer, Leaf82Serializer, Leaf82ListSerializer
from .models import Juso, Leaf82
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
import random
from rest_framework import status


User = get_user_model()


# 잎팔이 글 작성
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_leaf82(request):
    sido = request.data['sido']
    sigungu = request.data['sigungu']
    addr = get_object_or_404(Juso, sido=sido, sigungu=sigungu)
    user = request.user
    posting_addr = 0

    while posting_addr == 0:
        posting_addr = random.randint(100000, 999999)
        if Leaf82.objects.filter(user=user, posting_addr=posting_addr).exists():  # 중복체크, 한 유저 내에서 중복x
            posting_addr = 0

    serializer = Leaf82Serializer(data=request.data)
        
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=user, addr=addr, posting_addr=posting_addr)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 시도(지역) 검색
@api_view(['GET'])
def search_sido(request):
    data = Juso.objects.all()
    sido = []
    for s in data:
        sido_name = {
            "sido": s.sido
        }

        if sido and sido[-1] == sido_name:
            continue
        sido.append(sido_name)

    return Response(sido)


# 시군구(동네) 검색
@api_view(['GET'])
def search_sigungu(request, sido):
    sigungu = Juso.objects.filter(sido=sido).order_by('sigungu')
    serializer = JusoSigunguSerializer(sigungu, many=True)
    return Response(serializer.data)


from rest_framework.pagination import PageNumberPagination
from pagination import PaginationHandlerMixin
from rest_framework.views import APIView


class MemoPagination(PageNumberPagination):
    page_size_query_param = 'limit'
    
class Leaf82ListAPI(APIView, PaginationHandlerMixin):
    pagination_class = MemoPagination
    serializer_class = Leaf82ListSerializer
    def get(self, request, format=None, *args, **kwargs):
        instance = Leaf82.objects.all().order_by('-pk')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SearchAPI(APIView, PaginationHandlerMixin):
    pagination_class = MemoPagination
    serializer_class = Leaf82ListSerializer
    def get(self, request, format=None, *args, **kwargs):
        instance = Leaf82.objects.filter().order_by('-pk')

        plantname = request.GET.get('plantname', '*')
        sido = request.GET.get('sido', '*')
        sigungu = request.GET.get('sigungu', '*')
        category_class = request.GET.get('category_class', '분양해요')

        if plantname != '*':
            instance = instance.filter(plantname__contains=plantname)
            
        if sido != '*':
            addr1 = Juso.objects.filter(sido=sido)
            instance = instance.filter(addr__in=addr1)

        if sigungu != '*':
            addr2 = Juso.objects.filter(sigungu__contains=sigungu)
            instance = instance.filter(addr__in=addr2)

        instance = instance.filter(category_class=category_class)

        page = self.paginate_queryset(instance)        

        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page, many=True).data)
        else:
            serializer = self.serializer_class(instance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'DELETE'])
def detail_update_delete(request, username, posting_addr):
    user = get_object_or_404(User, username=username)
    leaf82 = get_object_or_404(Leaf82, user=user, posting_addr=posting_addr)

    def detail():
    
        serializer = Leaf82Serializer(leaf82)
        return Response(serializer.data)


    def update():
        request_copy_data = request.data.copy()

        if request_copy_data['photo'] == 'same':
            request_copy_data['photo'] = leaf82.photo

        if request.user == user:
            sido = request.data['sido']
            sigungu = request.data['sigungu']
            addr = get_object_or_404(Juso, sido=sido, sigungu=sigungu)
            serializer = Leaf82Serializer(instance=leaf82, data=request_copy_data)
            if serializer.is_valid(raise_exception=True):
                if request_copy_data['photo'] != '':
                    serializer.save(user=user, addr=addr, posting_addr=leaf82.posting_addr)

                else:
                    photo = 'static/monstera.jpg'
                    serializer.save(user=user, addr=addr, posting_addr=leaf82.posting_addr, photo=photo)
                return Response(serializer.data)
        else:
            return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)


    def delete():
        if request.user == user:
            leaf82.delete()
            return Response({'detail': '게시글이 삭제되었습니다.'})
        else:
            return Response({'detail': '잘못된 접근입니다.'}, status=status.HTTP_403_FORBIDDEN)

    if request.method == 'GET':
        return detail()
    elif request.method == 'PUT':
        return update()
    elif request.method == 'DELETE':
        return delete()
