from django.db import models
from userauth.models import User
from core.models import RontalModel


class NoteGroup(RontalModel):
    """
    Group dari notebook.
    """

    user = models.ForeignKey(User)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class NoteBook(RontalModel):
    """
    NoteBook berfungsi untuk menyimpan catatan kecil,
    atau pengingat (reminder)
    """

    user = models.ForeignKey(User)
    note_group = models.ForeignKey(NoteGroup)
    title = models.CharField(max_length=64)
    reminder_at = models.DateTimeField()
    note = models.TextField()

    def __unicode__(self):
        return self.title