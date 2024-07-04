import django.urls
import rest_framework.routers


router = rest_framework.routers.DefaultRouter()


urlpatterns = [
    django.urls.path("", django.urls.include(router.urls)),
]
