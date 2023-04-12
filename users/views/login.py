from django.contrib.auth import login
from rest_framework import permissions, status
from rest_framework import views
from rest_framework.response import Response

from users.serializers.login import LoginSerializer


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(
            {
                "token": str(user.auth_token)
            },
            status=status.HTTP_202_ACCEPTED
        )
