from userauth.models import Group, UserStatus, User, UserPassword, UserHistory
from django.contrib import admin
from core.admin import RontalAdmin


class GroupAdmin(RontalAdmin):
    """
    Administrasi Group
    """

    fields = ['name', 'description', 'is_protected']
    list_display = ('name', 'is_protected', 'description')


class UserStatusAdmin(RontalAdmin):
    """
    Administrasi User Status
    """

    fields = ['status', 'description', 'is_protected']
    list_display = ('status', 'is_protected', 'description')


class UserAdmin(RontalAdmin):
    """
    Administrasi User
    """
    fields = ['alias', 'email', 'group', 'user_status', 'is_protected']
    list_display = ('alias', 'is_protected', 'email', 'group', 'user_status')

    def queryset(self, request):
        return super(UserAdmin, self).queryset(request).filter(
                deleted_at__isnull=True,
                group__deleted_at__isnull=True,
                user__deleted_at__isnull=True)


class UserPasswordAdmin(RontalAdmin):
    """
    Administrasi Password (Sandi)
    """

    fields = ['user', 'password', 'is_protected']
    list_display = ('user', 'is_protected', 'password')

    def queryset(self, request):
        return super(UserPasswordAdmin, self).queryset(request).filter(
                deleted_at__isnull=True,
                user__deleted_at__isnull=True)


class UserHistoryAdmin(RontalAdmin):
    """
    Administrasi Log dari User
    """

    fields = ['user', 'user_log']
    list_display = ('user', 'user_log', 'created_at')

    def queryset(self, request):
        return super(UserHistoryAdmin, self).queryset(request).filter(
                deleted_at__isnull=True,
                user__deleted_at__isnull=True)


admin.site.register(Group, GroupAdmin)
admin.site.register(UserStatus, UserStatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserPassword, UserPasswordAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
