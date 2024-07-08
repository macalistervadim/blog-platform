import django.urls
import rest_framework.routers

import posts.views


router = rest_framework.routers.DefaultRouter()
router.register("posts", posts.views.PostViewSet, basename="posts")


urlpatterns = [
    django.urls.path("", django.urls.include(router.urls)),
    django.urls.path(
        "aside/",
        posts.views.AsideView.as_view(),
        name="aside-list",
    ),
    django.urls.path(
        "feedback/",
        posts.views.FeedBackView.as_view(),
        name="feedback",
    ),
    django.urls.path(
        "register/",
        posts.views.RegisterView.as_view(),
        name="register",
    ),
    django.urls.path("profile/", posts.views.ProfileView, name="profile"),
]
