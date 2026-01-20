from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User


class MyAtuhentication(BaseAuthentication):
    def authenticate(self, request):
        token = request.headers.get('mytoken')
        user = User.objects.get(username='admin')
        if token == '12345' and user:
            return (user, None)
        raise AuthenticationFailed('Invalid Token')