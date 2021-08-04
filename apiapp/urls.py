from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('members', views.MemberViewSet)

urlpatterns = [
    path('', include(router.urls))
]
# urlpatterns = [
#     path('members/', views.MemberList.as_view()),
#     path('members/<int:pk>', views.MemberDetail.as_view()),
# ]
