from rest_framework.views import APIView
from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from .serializers import NotificationSerializer
from  .models import Notification


class NotificationAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = NotificationSerializer

    def get(self, request, user_id, format=None):
        notifications_for_user = Notification.objects.filter(user__id=user_id).distinct()
        serializer = self.serializer_class(notifications_for_user, many=True)
        return Response(serializer.data)


class NotificationDetailAPIView(RetrieveDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (SessionAuthentication,)
    serializer_class = NotificationSerializer
    queryset = Notification.objects.all()
