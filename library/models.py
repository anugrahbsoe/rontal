from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from core.models import RontalModel
from userauth.models import User
import mimetypes
import shutil
from rontal import settings
import os


class Bookmark(RontalModel):
    """
    URL Bookmark situs yang menjadi referensi dalam penelitian Tugas Akhir.
    """

    user = models.ForeignKey(User)
    title = models.CharField(max_length=64)
    url = models.CharField(max_length=255)
    article_date = models.DateField()
    access_date = models.DateTimeField()
    description = models.CharField(max_length=255)
    cache = models.TextField()

    def __unicode__(self):
        return self.title


class ArchieveMimeType(RontalModel):
    """
    Mime-type yang diperbolehkan dalam penyimpanan arsip.
    """

    mime_type = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255)

    def __unicode__(self):
        return self.mime_type


class Archieve(RontalModel):
    """
    Arsip Tugas Akhir yang digunakan dalam penelitian, misalnya video, gambar,
    program, dll.
    """

    user = models.ForeignKey(User)
    mime_type = models.ForeignKey(ArchieveMimeType)
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=255)
    archieved_file = models.FileField(upload_to='uploads/%Y%m%d%H%M%S')

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.check_mime_type()
        return super(Archieve, self).save(*args, **kwargs)

    def check_mime_type(self):
        try:
            uri = self.archieved_file.path
        except:
            uri = self.archieved_file.url

        (ufile_mime_type, ufile_encoding) = mimetypes.guess_type(uri)

        try:
            file_type = ArchieveMimeType.objects.get(
                            mime_type=ufile_mime_type)
        except:
            raise ValidationError("Tipe file %s tidak valid" % self.mime_type)

        if self.pk is not None:
            arc = Archieve.objects.get(pk=self.pk)

            if arc.archieved_file != self.archieved_file:
                self.backup_file(arc.archieved_file)

    def backup_file(self, file_path):
        return shutil.move(
            os.path.dirname("%s/%s" % (settings.MEDIA_ROOT, file_path)),
            settings.MEDIA_TRASH)