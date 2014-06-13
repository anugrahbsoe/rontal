from library.models import Bookmark, ArchieveMimeType, Archieve
from django.contrib import admin
from core.admin import RontalAdmin


class BookmarkAdmin(RontalAdmin):
    """
    Administrasi Bookmark
    """

    fields = ['user', 'title', 'url', 'article_date', 'access_date']
    list_display = ('user', 'title', 'url', 'article_date',
                    'access_date')

    def queryset(self, request):
        return super(BookmarkAdmin, self).queryset(request).filter(
                deleted_at__isnull=True,
                user__deleted_at__isnull=True)


class ArchieveMimeTypeAdmin(RontalAdmin):
    """
    Administrasi Mime-type (jenis file) yang boleh di-upload
    """

    fields = ['mime_type', 'description', 'is_protected']
    list_display = ('mime_type', 'is_protected', 'description')


class ArchieveAdmin(RontalAdmin):
    """
    Administrasi arsip
    """

    fields = ['user', 'mime_type', 'title', 'description', 'archieved_file']
    list_display = ('title', 'user', 'mime_type', 'description')

    def queryset(self, request):
        return super(ArchieveAdmin, self).queryset(request).filter(
                deleted_at__isnull=True,
                user__deleted_at__isnull=True,
                mime_type__deleted_at__isnull=True)


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(ArchieveMimeType, ArchieveMimeTypeAdmin)
admin.site.register(Archieve, ArchieveAdmin)
