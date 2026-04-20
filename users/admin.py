from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from unfold.contrib.filters.admin import RangeDateFilter
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import History, User


@admin.register(User)
class UserModelAdmin(UserAdmin, ModelAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ["username", "first_name", "last_name"]
    model = User
    fieldsets = (
        (
            "Foydalanuvchini tahrirlash",
            {
                "fields": (
                    "username",
                    "first_name",
                    "last_name",
                    "password",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            "Yangi foydalanuvchi qo'shish",
            {
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                )
            },
        ),
    )


@admin.register(History)
class HistoryModelAdmin(ModelAdmin):
    list_display = ["user", "model", "comment", "created"]
    list_filter = (
        "user",
        "model",
        ("created", RangeDateFilter),
    )
