from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm

from accounts.models import CustomUser


class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name',)


class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm
    model = CustomUser
    list_display = ['last_name', 'first_name', 'middle_name', 'email', 'otdel', 'verify_user_access' , 'is_active', 'is_superuser']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username','last_name', 'first_name', 'middle_name', 'email', 'password1', 'password2', 'otdel','verify_user_access'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('username', 'last_name', 'first_name', 'middle_name', 'email', 'password','otdel', 'verify_user_access'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)