from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from unfold.contrib.filters.admin import RangeDateFilter


from .models import (
    Area,
    AccessControl,
    Department,
    Employee,
    OutputControl,
    Vocation,
)


class CoordinateInline(TabularInline):
    model = Area.coordinates.through
    extra = 0


@admin.register(Area)
class AreaModelAdmin(ModelAdmin):
    list_display = [
        "name",
    ]
    exclude = ("coordinates",)
    inlines = [CoordinateInline]


@admin.register(AccessControl)
class AccessControlModelAdmin(ModelAdmin):
    list_display = [
        "employee",
        "status",
        "created",
    ]
    search_fields = (
        "employee__full_name",
        "employee__handle",
    )
    list_filter = (
        "status",
        ("created", RangeDateFilter),
    )
    list_filter_submit = True


@admin.register(Department)
class DepartmentModelAdmin(ModelAdmin):
    list_display = [
        "name",
        "active",
    ]
    search_fields = ["name"]
    list_filter = ["active"]


@admin.register(Employee)
class EmployeeModelAdmin(ModelAdmin):
    list_display = [
        "full_name",
        "department",
        "position",
        "phone",
        "active",
    ]
    search_fields = (
        "full_name",
        "handle",
    )
    list_filter = (
        "department",
        "active",
    )


@admin.register(OutputControl)
class OutputControlModelAdmin(ModelAdmin):
    list_display = [
        "employee",
        "status",
        "created",
    ]


@admin.register(Vocation)
class VocationModelAdmin(ModelAdmin):
    list_display = [
        "employee",
        "start",
        "end",
    ]
    search_fields = (
        "employee__full_name",
        "employee__handle",
    )
    list_filter = (
        ("start", RangeDateFilter),
        ("end", RangeDateFilter),
    )
