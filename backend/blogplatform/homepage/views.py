import django.shortcuts


def homepageView(request):
    template = "index.html"

    return django.shortcuts.render(request, template)


def postDetailView(request):
    template = "post_detail.html"

    return django.shortcuts.render(request, template)


def contactFormView(request):
    template = "contact.html"

    return django.shortcuts.render(request, template)