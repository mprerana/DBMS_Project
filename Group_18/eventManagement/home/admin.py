from django.contrib import admin
from home.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.


class EmailConfirmInline(admin.StackedInline):
    model = EmailConfirm
    can_delete = False
    verbose_name_plural = 'EmailConfirm'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (EmailConfirmInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_select_related = ('emailconfirm', )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)



admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(user_rating)

