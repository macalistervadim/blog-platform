import django.urls

import homepage.views

app_name = "homepage"

urlpatterns = [
    django.urls.path("", homepage.views.homepageView, name="homepage"),
    django.urls.path("detail/", homepage.views.postDetailView, name="post_detail"),
    django.urls.path("contact/", homepage.views.contactFormView, name="contact"),
]