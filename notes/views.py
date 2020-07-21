from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from notes.serializers import UserSerializer, NoteCreateSerializer, NoteSerializer, UserAuthenticateSerializer
from notes.models import Note


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"status": "account created"}, status=status.HTTP_201_CREATED, headers=headers
        )


class NoteCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"status": "success"}, status=status.HTTP_201_CREATED, headers=headers
        )


class NoteListView(generics.ListAPIView):

    def get_queryset(self):
        user = self.request.GET.get("user_id")
        notes = Note.objects.filter(user_id=user)
        return notes

    serializer_class = NoteSerializer


class AuthenticateView(APIView):

    def get(self, request):
        serialized_user = UserAuthenticateSerializer(data=request.data)
        if serialized_user.is_valid(raise_exception=ValueError):
            user = authenticate(
                username=serialized_user.validated_data["username"],
                password=serialized_user.validated_data["password"]
            )
            if user is not None:
                return Response(
                    {
                        "status": "success",
                        "userId": user.id
                    },
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {
                        "status": "access denied"
                    },
                    status=status.HTTP_403_FORBIDDEN
                )
        else:
            return Response(
                {
                    "status": "bad data"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
