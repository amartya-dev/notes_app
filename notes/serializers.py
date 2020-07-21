from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.shortcuts import get_object_or_404

from notes.models import User, Note
from notes_app.utils import decrypt_note, encrypt_note


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=User.objects.all()
        )]
    )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ("username", "password")


class UserAuthenticateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    note = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = "__all__"

    def get_note(self, note_object):
        return decrypt_note(note_object.note)


class NoteCreateSerializer(serializers.ModelSerializer):
    note = serializers.CharField()

    def create(self, validated_data):
        encrypted_note = encrypt_note(validated_data["note"])
        note_object = Note.objects.create(
            note=encrypted_note,
            user=validated_data["user"]
        )
        return note_object

    class Meta:
        model = Note
        fields = "__all__"
