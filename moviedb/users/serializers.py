from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True,
                                     validators=[UniqueValidator(queryset=Account.objects.all())])
    password = serializers.CharField(min_length=8,
                                     write_only=True,
                                     required=True)

    class Meta:
        model = Account
        fields = ['id', 'username', 'password', 'followed_genres', 'followed_artists']

    def create(self, validated_data):
        username = validated_data.get('username', None)
        password = validated_data.get('password', None)
        if username and password:
            user_account = Account.objects.create_user(username=username)
            user_account.set_password(password)
            user_account.save()
        else:
            raise serializers.ValidationError('A username and password is required to sign up')
        return user_account

    def update(self, instance, validated_data):
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)

        followed_genres = validated_data.get('followed_genres', [])
        if followed_genres:
            instance.followed_genres.set(followed_genres)

        followed_artists = validated_data.get('followed_artists', [])
        if followed_artists:
            instance.followed_artists.set(followed_artists)

        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get('username', None)
        password = data.get('password', None)

        if username and password:
            user = authenticate(username=username,
                                password=password)

        else:
            raise serializers.ValidationError('A username and password is required to sign in')

        if not user:
            raise serializers.ValidationError('Incorrect username or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}
