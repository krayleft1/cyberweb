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
    list_display = ['email', 'last_name', 'is_active', 'is_superuser']
    add_fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'middle_name', 'email', 'password1', 'password2', 'otdel','Verify'),
        }),
    )
    fieldsets = (
        (None, {
            'fields': ('first_name', 'last_name', 'middle_name', 'email', 'password','otdel', 'Verify'),
        }),
    )


admin.site.register(CustomUser, CustomUserAdmin)
