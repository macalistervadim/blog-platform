import django.conf
import django.contrib
import django.urls
import rest_framework_simplejwt.views

urlpatterns = [
    django.urls.path("admin/", django.contrib.admin.site.urls),
    django.urls.path("api/v1/", django.urls.include("api.urls")),
    django.urls.path(
        "api/v1/token/",
        rest_framework_simplejwt.views.TokenObtainPairView.as_view(),
        name="token",
    ),
    django.urls.path(
        "api/v1/refresh_token/",
        rest_framework_simplejwt.views.TokenRefreshView.as_view(),
        name="refresh_token",
    ),
    django.urls.path(
        "ckeditor/",
        django.urls.include("ckeditor_uploader.urls"),
    ),
]


if django.conf.settings.DEBUG:
    import debug_toolbar
    import django.conf.urls.static

    STATIC_ROOT = django.conf.urls.static.static

    urlpatterns += (
        [
            django.urls.path(
                "__debug__/",
                django.urls.include(debug_toolbar.urls),
            ),
        ]
        + STATIC_ROOT(
            django.conf.settings.STATIC_URL,
            document_root=django.conf.settings.STATICFILES_DIRS,
        )
        + STATIC_ROOT(
            django.conf.settings.MEDIA_URL,
            document_root=django.conf.settings.MEDIA_ROOT,
        )
    )
