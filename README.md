Django REST Framework: Function-Based View vs Class-Based View

A practical comparison between "@api_view" (Function-Based View) and "APIView" (Class-Based View) in Django REST Framework.

This documentation demonstrates how to implement the same API features using both approaches.

---

1. Basic Structure

Function-Based View ("@api_view")

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def student_api(request):
    return Response({"message": "Hello World"})

Class-Based View ("APIView")

from rest_framework.views import APIView
from rest_framework.response import Response

class StudentAPI(APIView):

    def get(self, request):
        return Response({"message": "Hello World"})

Main Difference:

- Function uses "@api_view" decorator.
- Class uses "APIView" inheritance.

---

2. HTTP Methods (GET, POST, PUT, PATCH, DELETE)

Function-Based View

@api_view(['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])
def student_api(request):

    if request.method == 'GET':
        return Response({"message": "Get Data"})

    elif request.method == 'POST':
        return Response({"message": "Create Data"})

    elif request.method == 'PUT':
        return Response({"message": "Update Data"})

    elif request.method == 'PATCH':
        return Response({"message": "Partial Update"})

    elif request.method == 'DELETE':
        return Response({"message": "Delete Data"})

Class-Based View

class StudentAPI(APIView):

    def get(self, request):
        return Response({"message": "Get Data"})

    def post(self, request):
        return Response({"message": "Create Data"})

    def put(self, request):
        return Response({"message": "Update Data"})

    def patch(self, request):
        return Response({"message": "Partial Update"})

    def delete(self, request):
        return Response({"message": "Delete Data"})

Main Difference:

- Function: "if request.method == 'GET'"
- Class: "def get(self, request)"

---

3. Request Data

Function-Based View

@api_view(['POST'])
def student_api(request):

    name = request.data.get('name')
    age = request.data.get('age')

    return Response({
        "name": name,
        "age": age
    })

Class-Based View

class StudentAPI(APIView):

    def post(self, request):

        name = request.data.get('name')
        age = request.data.get('age')

        return Response({
            "name": name,
            "age": age
        })

Main Difference: No difference in "request.data".

---

4. Query Parameters

Example URL:

/students/?name=Rahim

Function-Based View

@api_view(['GET'])
def student_api(request):

    name = request.query_params.get('name')

    return Response({"name": name})

Class-Based View

class StudentAPI(APIView):

    def get(self, request):

        name = request.query_params.get('name')

        return Response({"name": name})

Main Difference: Both use "request.query_params".

---

5. Serializer

Function-Based View

@api_view(['POST'])
def student_api(request):

    serializer = StudentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)

Class-Based View

class StudentAPI(APIView):

    def post(self, request):

        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=400)

Main Difference: Serializer usage is exactly the same.

---

6. Authentication

Function-Based View

from rest_framework.decorators import (
    api_view,
    authentication_classes
)
from rest_framework.authentication import TokenAuthentication

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def student_api(request):

    return Response({"message": "Authenticated"})

Class-Based View

from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication

class StudentAPI(APIView):

    authentication_classes = [TokenAuthentication]

    def get(self, request):

        return Response({"message": "Authenticated"})

Main Difference:

- Function: "@authentication_classes([...])"
- Class: "authentication_classes = [...]"

---

7. Permission

Function-Based View

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def student_api(request):

    return Response({"message": "Access Granted"})

Class-Based View

from rest_framework.permissions import IsAuthenticated

class StudentAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return Response({"message": "Access Granted"})

Main Difference:

- Function: "@permission_classes([...])"
- Class: "permission_classes = [...]"

---

8. Throttling

Function-Based View

from rest_framework.decorators import throttle_classes
from rest_framework.throttling import UserRateThrottle

@api_view(['GET'])
@throttle_classes([UserRateThrottle])
def student_api(request):

    return Response({"message": "Hello"})

Class-Based View

from rest_framework.throttling import UserRateThrottle

class StudentAPI(APIView):

    throttle_classes = [UserRateThrottle]

    def get(self, request):

        return Response({"message": "Hello"})

Main Difference:

- Function: "@throttle_classes([...])"
- Class: "throttle_classes = [...]"

---

9. Pagination

Both approaches can use "PageNumberPagination".

Function-Based View

@api_view(['GET'])
def student_api(request):

    students = Student.objects.all()

    paginator = PageNumberPagination()
    paginator.page_size = 5

    result = paginator.paginate_queryset(
        students, request
    )

    serializer = StudentSerializer(result, many=True)

    return paginator.get_paginated_response(serializer.data)

Class-Based View

class StudentAPI(APIView):

    def get(self, request):

        students = Student.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = 5

        result = paginator.paginate_queryset(
            students, request
        )

        serializer = StudentSerializer(result, many=True)

        return paginator.get_paginated_response(serializer.data)

Main Difference: Pagination logic is the same in both.

---

10. Filtering and Search

Function-Based View

@api_view(['GET'])
def student_api(request):

    students = Student.objects.all()

    search = request.query_params.get('search')

    if search:
        students = students.filter(
            name__icontains=search
        )

    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)

Class-Based View

class StudentAPI(APIView):

    def get(self, request):

        students = Student.objects.all()

        search = request.query_params.get('search')

        if search:
            students = students.filter(
                name__icontains=search
            )

        serializer = StudentSerializer(students, many=True)

        return Response(serializer.data)

Main Difference: Both use the same Django ORM and query parameters.

---

11. URL Configuration

Function-Based View

from django.urls import path
from .views import student_api

urlpatterns = [
    path('students/', student_api),
]

Class-Based View

from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/', StudentAPI.as_view()),
]

Main Difference:

- Function: Direct function reference.
- Class: Must use ".as_view()".

---

12. Complete Difference Table

Feature| @api_view| APIView
View Type| Function Based| Class Based
Structure| Function| Class
GET| request.method| get()
POST| request.method| post()
PUT| request.method| put()
PATCH| request.method| patch()
DELETE| request.method| delete()
Request Data| Same| Same
Query Params| Same| Same
Serializer| Same| Same
Validation| Same| Same
Response| Same| Same
Authentication| Decorator| Class Attribute
Permission| Decorator| Class Attribute
Throttling| Decorator| Class Attribute
Pagination| Manual| Manual
Filtering| Manual| Manual
URL| Function Name| as_view()
Inheritance| No| Yes
Code Reusability| Limited| Better

---

13. When Should You Use Which?

Use "@api_view" When:

- Building small APIs.
- Creating simple CRUD operations.
- Writing quick API endpoints.
- Working with simple business logic.

Use "APIView" When:

- Building complex APIs.
- Organizing code using classes.
- Using inheritance.
- Creating reusable class-based structures.
- Managing multiple HTTP methods separately.

---

14. Important Learning Path

Recommended Django REST Framework learning sequence:

1. Function-Based Views ("@api_view")
2. Class-Based Views ("APIView")
3. GenericAPIView
4. Generic Views
5. Mixins
6. ViewSets
7. ModelViewSet
8. Routers

---

Conclusion

Both "@api_view" and "APIView" provide similar REST API capabilities.

The main difference is their structure and configuration style.

Remember:

- "@api_view" = Function-Based API Development.
- "APIView" = Class-Based API Development.

Both support CRUD, Serializers, Authentication, Permissions, Pagination, Filtering and other REST framework features.

Happy Learning! 🚀
