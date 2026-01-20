
from django.urls import path,include
from . import views


# For Simple JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)



# Model ViewSet and router

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('infoo', views.StudentModelViewSet, basename='stuinfo'),
router.register('readonlyinfo', views.StudentReadOnlyModelViewSet,basename='stureadonlyinfo'),

router.register('singer', views.SingerViewSet, basename='singer'),
router.register('song', views.SongViewSet, basename='song'),


urlpatterns = [
    path('index/', views.index ),




    # .........FUNCTION BASED VIEW........
    # path('api/info/', views.info ),
    # path('api/info/<int:id>/', views.info ),



    # ........CLASS BASED VIEW............
    # path('api/info/', views.Info.as_view() ),
    # path('api/info/<int:id>/', views.Info.as_view() ),




    # .........GENERIC CLASS BASED VIEW...........
    # path('stul/', views.StudentList.as_view()),
    # path('stuc/', views.StudentCreate.as_view()),
    # path('stur/<int:pk>/', views.StudentRetrieve.as_view()),
    # path('stup/<int:pk>/', views.StudentUpdate.as_view()),
    # path('stud/<int:pk>/', views.StudentDestroy.as_view()),
    # path('stu_ru/<int:pk>/', views.StudentRetrieveUpdate.as_view()),
    # path('stu_rd/<int:pk>/', views.StudentRetrieveDestroy.as_view()),

    # path('stu_lc/', views.StudentListCreate.as_view()),
    # path(' /<int:pk>/', views.StudentRetrieveUpdateDestroy.as_view()),



    #...........Model view set and router.....
    path('', include(router.urls)),


    #.........for session authentication.......
    # path('auth/', include('rest_framework.urls'), name='rest_framework_urls'),



    # .........For Simple JWT...........
    path('gettoken/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verifytoken/', TokenVerifyView.as_view(), name='token_verify'),




]
