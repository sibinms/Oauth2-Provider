from oauth2_provider.contrib.rest_framework.authentication import OAuth2Authentication
from oauth2_provider.models import AccessToken
from rest_framework.response import Response

from rest_framework.generics import ListAPIView, GenericAPIView


class ApiEndpoint(GenericAPIView):
    authentication_classes = [OAuth2Authentication]

    def get(self, request, *args, **kwargs):
        print(request.auth)
        token = request.auth
        access_token = AccessToken.objects.get(token=token)
        claims = {
            "sub": str(access_token.user.id),
            'email': access_token.user.email
        }
        return Response(claims)
