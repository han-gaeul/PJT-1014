from unicodedata import name
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    # 작성/수정 페이지
    path('create/', views.create, name='create'),
    # 목록 조회
    path('index/', views.index, name='index'),
    # 정보 조회
    path('<int:pk>/', views.detail, name='detail'),
    # 수정 페이지
    path('<int:pk>/update/', views.update, name='update'),
    # 삭제
    path('<int:pk>/delete/', views.delete, name='delete'),
]
