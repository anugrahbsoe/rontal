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


class UserPasswordAdmin(RontalAdmin):
    """
    Administrasi Password (Sandi)
    """
    
    fields = ['user', 'password', 'is_protected']
    list_display = ('user', 'is_protected', 'password')


class UserHistoryAdmin(RontalAdmin):
    """
    Administrasi Log dari User
    """
    
    fields = ['user', 'user_log']
    list_display = ('user', 'user_log', 'created_at')


admin.site.register(Group, GroupAdmin)
admin.site.register(UserStatus, UserStatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserPassword, UserPasswordAdmin)
admin.site.register(UserHistory, UserHistoryAdmin)
