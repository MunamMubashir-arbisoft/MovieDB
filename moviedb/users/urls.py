from django.urls import path
from .views import RegisterAPIView, LoginAPIView, LogoutAPIView, AccountDetailAPIView

app_name = 'users'
urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register_user'),
    path('login/', LoginAPIView.as_view(), name='login_user'),
    path('logout/', LogoutAPIView.as_view(), name='logout_user'),
    path('profile/', AccountDetailAPIView.as_view(), name='user_detail')
]
