import datetime
import os
import pathlib

import dotenv


dotenv.load_dotenv()


def load_bool(name, default):
    value = os.getenv(name, str(default)).lower()
    return value in ("", "true", "True", "t", "y", "yes", "YES", "1")


def load_list(name, default):
    return os.getenv(name, str(default)).split(",")


BASE_DIR = pathlib.Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", default="key")

DEBUG = load_bool("DJANGO_DEBUG", default="False")

ALLOWED_HOSTS = load_list("DJANGO_ALLOWED_HOSTS", default="*")

INSTALLED_APPS = [
    "api.apps.ApiConfig",
    "posts.apps.PostsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "ckeditor",
    "ckeditor_uploader",
    "taggit",
    "taggit_serializer",
    "django_cleanup.apps.CleanupConfig",
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

if DEBUG:
    INSTALLED_APPS.append(
        "debug_toolbar",
    )
    MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
    INTERNAL_IPS = ["127.0.0.1", "localhost"]

ROOT_URLCONF = "blogplatform.urls"

TEMPLATES_DIRS = BASE_DIR / "templates"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [TEMPLATES_DIRS],
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

WSGI_APPLICATION = "blogplatform.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Europe/Moscow"

USE_I18N = True

USE_TZ = True

LOGIN_URL = os.getenv("DJANGO_LOGIN_URL", default="/api/v1/signin")

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(
        minutes=int(os.getenv("SIMPLE_JWT_ACCESS_TOKEN_LIFETIME", 30)),
    ),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(
        days=int(os.getenv("SIMPLE_JWT_REFRESH_TOKEN_LIFETIME", 2)),
    ),
}

CORS_ORIGIN_WHITELIST = load_list("CORS_ORIGIN_WHITELIST", default="*")

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"],
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PERMISSION_CLASSES": (
        "rest_framework.permissions.DjangoModelPermissions",
    ),
    "SEARCH_PARAM": "q",
}

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static_dev"]
STATIC_ROOT = BASE_DIR / "static"

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CKEDITOR_JQUERY_URL = (
    "https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"
)

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_IMAGE_BACKEND = "pillow"

CKEDITOR_CONFIGS = {
    "default": {
        "skin": "moono",
        "toolbar_Basic": [["Source", "-", "Bold", "Italic"]],
        "toolbar_YourCustomToolbarConfig": [
            {
                "name": "document",
                "items": [
                    "Source",
                    "-",
                    "Save",
                    "NewPage",
                    "Preview",
                    "Print",
                    "-",
                    "Templates",
                ],
            },
            {
                "name": "clipboard",
                "items": [
                    "Cut",
                    "Copy",
                    "Paste",
                    "PasteText",
                    "PasteFromWord",
                    "-",
                    "Undo",
                    "Redo",
                ],
            },
            {"name": "editing", "items": ["Find", "Replace", "-", "SelectAll"]},
            {
                "name": "forms",
                "items": [
                    "Form",
                    "Checkbox",
                    "Radio",
                    "TextField",
                    "Textarea",
                    "Select",
                    "Button",
                    "ImageButton",
                    "HiddenField",
                ],
            },
            "/",
            {
                "name": "basicstyles",
                "items": [
                    "Bold",
                    "Italic",
                    "Underline",
                    "Strike",
                    "Subscript",
                    "Superscript",
                    "-",
                    "RemoveFormat",
                ],
            },
            {
                "name": "paragraph",
                "items": [
                    "NumberedList",
                    "BulletedList",
                    "-",
                    "Outdent",
                    "Indent",
                    "-",
                    "Blockquote",
                    "CreateDiv",
                    "-",
                    "JustifyLeft",
                    "JustifyCenter",
                    "JustifyRight",
                    "JustifyBlock",
                    "-",
                    "BidiLtr",
                    "BidiRtl",
                    "Language",
                ],
            },
            {"name": "links", "items": ["Link", "Unlink", "Anchor"]},
            {
                "name": "insert",
                "items": [
                    "Image",
                    "Flash",
                    "Table",
                    "HorizontalRule",
                    "Smiley",
                    "SpecialChar",
                    "PageBreak",
                    "Iframe",
                ],
            },
            "/",
            {
                "name": "styles",
                "items": ["Styles", "Format", "Font", "FontSize"],
            },
            {"name": "colors", "items": ["TextColor", "BGColor"]},
            {"name": "tools", "items": ["Maximize", "ShowBlocks"]},
            {"name": "about", "items": ["About"]},
            "/",
            {
                "name": "yourcustomtools",
                "items": [
                    "Preview",
                    "Maximize",
                ],
            },
        ],
        "toolbar": "YourCustomToolbarConfig",
        "tabSpaces": 4,
        "extraPlugins": ",".join(
            [
                "uploadimage",
                "div",
                "autolink",
                "autoembed",
                "embedsemantic",
                "autogrow",
                "widget",
                "lineutils",
                "clipboard",
                "dialog",
                "dialogui",
                "elementspath",
            ],
        ),
    },
}

EMAIL_BACKEND = os.getenv("DJANGO_EMAIL_BACKEND")

EMAIL_HOST = os.getenv("DJANGO_EMAIL_HOST")

EMAIL_PORT = int(os.getenv("DJANGO_EMAIL_PORT"))

EMAIL_USE_SSL = os.getenv("DJANGO_EMAIL_USE_SSL") == "True"

EMAIL_HOST_USER = os.getenv("DJANGO_EMAIL_HOST_USER")

EMAIL_HOST_PASSWORD = os.getenv("DJANGO_EMAIL_HOST_PASSWORD")

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER

EMAIL_ADMIN = EMAIL_HOST_USER

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'console': {
#             'format': '%(name)-12s %(levelname)-8s %(message)s'
#         },
#         'file': {
#             'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
#         },
#     },
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#             'formatter': 'console',
#         },
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'formatter': 'file',
#             'filename': os.path.join(BASE_DIR, 'debug.log'),
#         },
#     },
#     'loggers': {
#         '': {
#             'level': 'DEBUG',
#             'handlers': ['console', 'file'],
#         },
#         'django': {
#             'handlers': ['console', 'file'],
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#         'django.request': {
#             'handlers': ['file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }

# logging.config.dictConfig(LOGGING)
