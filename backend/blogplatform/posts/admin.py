import django.contrib.admin

import posts.models


django.contrib.admin.site.register(posts.models.Post)
