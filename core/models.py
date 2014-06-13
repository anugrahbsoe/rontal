from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class RontalModel(models.Model):
    """Rontal model dengan fasilitas soft delete"""

    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    deleted_at = models.DateTimeField(default=None, null=True)
    is_protected = models.BooleanField(default=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.created_at = timezone.now()
        elif self.deleted_at is not None:
            raise ValidationError("Gagal menyimpan %s" % self)

        self.updated_at = timezone.now()
        return super(RontalModel, self).save(*args, **kwargs)

    def delete(self):
        if self.is_protected or self.deleted_at is not None:
            raise ValidationError("Gagal menghapus %s" % self)
        else:
            self.deleted_at = timezone.now()

        return super(RontalModel, self).save()