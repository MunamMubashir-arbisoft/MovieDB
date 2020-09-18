from rest_framework import serializers

from .models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    message = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Notification
        fields = ['id', 'message', 'movie', 'created_at']
