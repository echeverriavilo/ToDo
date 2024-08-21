from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Task, UserProfile
from .forms import ProfileForm

admin.site.register(Task)

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    form = ProfileForm
    can_delete = False
    verbose_name_plural = 'Profile'
    fields = ['name', 'age', 'email', 'phone_number']
    
    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 1
        return 0

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    
    def get_inline_instances(self, request, obj=None):
        inline_instances = super().get_inline_instances(request, obj)
        if obj is not None:
            return inline_instances
        return inline_instances

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'age', 'email', 'phone_number')
    search_fields = ('user__username', 'name', 'email')
    list_filter = ('age',)