from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from notes.models import User, Note


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(
        max_length=150,
        validators=UniqueValidator(
            queryset=User.objects.all()
        )
    )

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ("username", "password")


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Note
        fields = "__all__"


class NoteCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
