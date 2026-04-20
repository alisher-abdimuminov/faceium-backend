from pathlib import Path
from django.urls import reverse_lazy


BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = "django-insecure-wj#=3_0onbp^n+kq=5teqai#vok1&om2gxbrg#h8jkk4@toa7z"

DEBUG = True

ALLOWED_HOSTS = ["*"]


INSTALLED_APPS = [
    # unfold
    "unfold",
    "unfold.contrib.filters",
    # django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # external
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    # local
    "users",
    "employees",
    "api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

AUTH_PASSWORD_VALIDATORS = []


LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Tashkent"

USE_I18N = True

USE_TZ = True


STATIC_URL = "static/"
STATIC_ROOT = "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Additional settings

AUTH_USER_MODEL = "users.User"

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "https://api.fc.uzfi.uz",
    "http://localhost:8000",
    "https://api.fc.samdpi.uz",
]
# SESSION_COOKIE_DOMAIN = ".fc.uzfi.uz"
# CSRF_COOKIE_DOMAIN = ".fc.uzfi.uz"
CSRF_COOKIE_SECURE = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
}

UNFOLD = {
    "SITE_TITLE": "Admin Panel",
    "SITE_HEADER": "Face Control",
    "SITE_SUBHEADER": "Admin Panel",
    "SITE_ICON": {
        "light": lambda request: (
            "https://samdpi.uz/static/assets2/images/logo/samDPI.png"
        ),
        "dark": lambda request: (
            "https://samdpi.uz/static/assets2/images/logo/samDPI.png"
        ),
    },
    "SHOW_HISTORY": True,
    "SIDEBAR": {
        "show_search": True,
        "navigation": [
            {
                "title": "Asosiy",
                "separator": True,
                "collapsable": True,
                "items": [
                    {
                        "title": "Xodimlar",
                        "icon": "person",
                        "link": reverse_lazy("admin:employees_employee_changelist"),
                    },
                    {
                        "title": "Bo'limlar",
                        "icon": "account_balance",
                        "link": reverse_lazy("admin:employees_department_changelist"),
                    },
                    {
                        "title": "Davomat",
                        "icon": "edit_note",
                        "link": reverse_lazy(
                            "admin:employees_accesscontrol_changelist"
                        ),
                    },
                    {
                        "title": "Ta'til",
                        "icon": "celebration",
                        "link": reverse_lazy("admin:employees_vocation_changelist"),
                    },
                    {
                        "title": "Joylashuvlar",
                        "icon": "location_on",
                        "link": reverse_lazy("admin:employees_area_changelist"),
                    },
                    {
                        "title": "Foydalanuvchilar",
                        "icon": "account_circle",
                        "link": reverse_lazy("admin:users_user_changelist"),
                    },
                    {
                        "title": "Tarix",
                        "icon": "history",
                        "link": reverse_lazy("admin:users_history_changelist"),
                    },
                ],
            }
        ],
    },
}
