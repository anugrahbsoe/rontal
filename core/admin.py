from django.contrib import admin


class RontalAdmin(admin.ModelAdmin):
    """Admin dengan fasilitas soft delete"""

    actions = ['soft_delete']

    def soft_delete(self, request, queryset):
        for object in queryset:
            object.delete()

    soft_delete.short_description = "Delete selected items"

    def get_actions(self, request):
        actions = super(RontalAdmin, self).get_actions(request)
        del actions['delete_selected']
        return actions

    def queryset(self, request):
        return super(RontalAdmin, self).queryset(request).filter(
                    deleted_at__isnull=True)