from django.urls import path, include

from .views import check_location, check_handle, faceid, make_word


urlpatterns = [
    path("auth/", include("users.urls")),
    path("employees/", include("employees.urls")),

    path("location/", check_location, name="check_location"),
    path("handle/", check_handle, name="check_passport"),
    path("faceid/", faceid, name="faceid"),
    path("make_word/", make_word, name="make_word"),
]
