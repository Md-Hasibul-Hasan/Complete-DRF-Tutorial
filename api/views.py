from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt



from .models import *
from .serializers import *

from rest_framework.authentication import BaseAuthentication, SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly
from .custom_permissions import MyPermission
from .custom_auth import MyAtuhentication

# Create your views here.
@csrf_exempt
def index(request):
    stu = [
        Student(name='A', roll=1, city='a'), Student(name='B', roll=2, city='b'), Student(name='C', roll=3, city='c')
        ]
    # res = Student.objects.bulk_create(stu)
    # res = Student.objects.exclude(id__lt=16).delete()
    res = Student.objects.all().values()
    return JsonResponse({'msg': 'Data Created','data':list(res)})


'''

# Function Based API View

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404



@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def info(request, id=None):


    # ---------- GET ----------
    if request.method == 'GET':

        if id is not None:
            stu = get_object_or_404(Student, id=id)
            serializer = StudentSerializer(stu)

            return Response(
                {
                    "msg": "Single Data",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

        else:

            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)

            return Response(
                {
                    "msg": "All Data",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )

    # ---------- POST ----------
    if request.method == 'POST':
        dt = request.data
        print(dt)
        serializer = StudentSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "Data Created",
                    "data": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            return Response(
                {
                    "msg": "Data Not Created",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

    # ---------- PUT ----------
    if request.method == 'PUT':
        dt = request.data
        stu = get_object_or_404(Student, id=id)
        print(stu)
        serializer = StudentSerializer(stu, data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "Complete Data Updated",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "msg": "Data Not Updated",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )


    # ---------- PATCH ----------
    if request.method == 'PATCH':
        dt = request.data
        stu = get_object_or_404(Student, id=id)
        print(stu)
        serializer = StudentSerializer(stu, data=dt, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "msg": "Partial Data Updated",
                    "data": serializer.data
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {
                    "msg": "Data Not Updated",
                    "data": serializer.errors
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        

    # ---------- DELETE ----------
    if request.method == 'DELETE':
        stu = get_object_or_404(Student, id=request.data.get('id'))
        stu.delete()
        return Response(
            {
                "msg": "Data Deleted",
            },
            status=status.HTTP_200_OK
        )


'''     

'''

# Class Based ApiView 

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class Info(APIView): 

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

 

    def get(self, request, id=None):
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response({'msg': 'Single Data', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response({'msg': 'All Data', 'data': serializer.data}, status=status.HTTP_200_OK)
        


    def post(self, request):
        dt = request.data
        serializer = StudentSerializer(data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Created', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def put(self, request, id):
        dt = request.data
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=dt)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Complete Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def patch(self, request, id):
        dt = request.data
        stu = Student.objects.get(id=id)
        serializer = StudentSerializer(stu, data=dt, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated', 'data': serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def delete(self, request, id):
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({'msg': 'Data Deleted'}, status=status.HTTP_200_OK)
    

'''


'''
# .................. Concrete generic class based view...........................

from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, ListCreateAPIView , RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView



class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentCreate(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieve(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentUpdate(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDestroy(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveDestroy(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# ----------main two ----------

class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
  
'''




# '''

# Model view set

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from .throtling import MyRateThrottle
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle, ScopedRateThrottle

# for search and filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

# for pagination 
from .paginations import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    # throttle_classes = [MyRateThrottle]

    filter_backends = [DjangoFilterBackend, SearchFilter,OrderingFilter]
    filterset_fields = ['name', 'city']  #Give exact matches : name='HASIB
    search_fields = ['name', 'city']     #Find text containing keyword : name='has'
    ordering_fields = ['name', 'roll']
    # ordering = ['-created_at'] # Default ordering

    pagination_class = MyPageNumberPagination
    # pagination_class = MyLimitOffsetPagination
    # pagination_class = MyCursorPagination

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'scoped'



class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


# '''







