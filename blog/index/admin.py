from django.contrib import admin
from .models import *
admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(File)
admin.site.register(Social)
admin.site.register(Comment)
admin.site.register(Slider)
admin.site.register(SubNavigation)
admin.site.register(Navigation)
admin.site.register(Category)
@admin.register(Setting)
class AuthorAdmin(admin.ModelAdmin):
    # to disbale add functionality
    def has_add_permission(self, request):
        return False

    # to disable delete functionaliyt
    def has_delete_permission(self, request, obj=None):
        return False