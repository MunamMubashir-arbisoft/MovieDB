from django.urls import path

from .views import NotificationAPIView, NotificationDetailAPIView


app_name = 'notifications'
urlpatterns = [
    path('user=<int:user_id>/', NotificationAPIView.as_view(), name='user_notifications'),
    path('<int:pk>/', NotificationDetailAPIView.as_view(), name='notification_detail')
]
