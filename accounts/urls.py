from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    # 회원가입 페이지
    path('signup/', views.signup, name='signup'),
    # 로그인 페이지
    path('login/', views.login, name='login'),
    # 회원 목록 페이지
    path('index/', views.index, name='index'),
    # 회원 정보 페이지
    path('detail/', views.detail, name='detail'),
    # 회원 정보 수정 페이지
    path('update/', views.update, name='update'),
    # 로그아웃
    path('logout/', views.logout, name='logout'),
]
