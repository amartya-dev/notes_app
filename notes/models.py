from django.db import models
from django.contrib.auth.models import User

from notes.utils import encrypt_note


class Note(models.Model):
    note = models.TextField()
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='notes'
    )

    # Override the save function to automatically encrypt the note before saving
    def save(self, *args, **kwargs):
        self.note = encrypt_note(note=self.note)
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
        return self.note[:10] + "..."
