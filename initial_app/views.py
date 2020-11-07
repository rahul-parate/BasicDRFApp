from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from initial_app.serializers import UserSerializer, DataSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Profile

from .serializers import RegistrationSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


import logging

logger = logging.getLogger(__name__)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Registration(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):

        try:
            serializer = RegistrationSerializer(data=request.data)
            if serializer.is_valid():
                validated_data = serializer.validated_data
                created, profile_id, message = serializer.create(
                    validated_data=validated_data)
                if created:
                    tokenr = TokenObtainPairSerializer().\
                    get_token(request.user)
                    tokena = AccessToken().for_user(request.user)
                    logged_in_user = User.objects.get(id=profile_id)
                    return Response(
                        {
                            'created': True,
                            'user_id': profile_id
                        },
                        status=status.HTTP_200_OK)
                else:
                    print(logger)
                    logger.debug('Error')
                    return Response(
                        {
                            'message': message
                        },
                        status=status.HTTP_400_BAD_REQUEST) 
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)
            logger.errors(e)
            return Response(
                {'message': 'Issue'},
                status=status.HTTP_409_CONFLICT)

class Getdata(APIView):

    def get(self, request, *args, **kwargs):

        queryset = Profile.objects.all()

        serializer = DataSerializer(queryset, many=True)

        print(serializer.data)
        return Response(
                {
                'ok': True,
                'members': serializer.data
                },
                status=status.HTTP_200_OK
            )
