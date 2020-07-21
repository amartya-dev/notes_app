from django.db import models
from django.contrib.auth.models import User

from notes_app.utils import encrypt_note


class Note(models.Model):
    note = models.BinaryField()
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    def __str__(self):
        return self.user.username + "Note number : " + str(self.id)
