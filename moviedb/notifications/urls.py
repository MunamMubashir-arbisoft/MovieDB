from django.urls import path
from .views import NotificationAPIView

app_name = 'notifications'
urlpatterns = [
    path('<int:user_id>/', NotificationAPIView.as_view(), name='user_notifications')
]
