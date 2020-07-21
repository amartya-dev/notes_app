from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

from notes.serializers import UserSerializer, NoteCreateSerializer, NoteSerializer
from notes.models import Note


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NoteCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Note.objects.all()
    serializer_class = NoteCreateSerializer


class NoteListView(generics.ListAPIView):

    def get_queryset(self):
        user = self.request.GET.get("user_id")
        notes = Note.objects.filter(user_id=user)
        return notes

    serializer_class = NoteSerializer
