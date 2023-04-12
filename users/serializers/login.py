from django.contrib.auth import authenticate
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=True
    )
    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(
                request=self.context.get('request'),
                username=username,
                password=password
            )
            if not user:
                msg = 'No user match for credentials you have provided'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Both "username" and "password" are required.'
            raise serializers.ValidationError(msg)
        attrs['user'] = user
        return attrs
