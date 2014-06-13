from notebook.models import NoteGroup, NoteBook
from django.contrib import admin
from core.admin import RontalAdmin


class NoteGroupAdmin(RontalAdmin):
    """
    Administrasi Note Group
    """

    fields = ['name', 'user', 'description']
    list_display = ('user', 'name', 'description')


class NoteBookAdmin(RontalAdmin):
    """
    NoteBook Admin
    """

    fields = ['user', 'note_group', 'title', 'reminder_at', 'note']
    list_display = ('title', 'note_group', 'reminder_at', 'user')

    def queryset(self, request):
        return super(NoteBookAdmin, self).queryset(request).filter(
                    deleted_at__isnull=True,
                    note_group__deleted_at__isnull=True)


admin.site.register(NoteGroup, NoteGroupAdmin)
admin.site.register(NoteBook, NoteBookAdmin)