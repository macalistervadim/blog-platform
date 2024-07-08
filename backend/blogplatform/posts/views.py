import django.core.mail
import rest_framework.filters
import rest_framework.pagination
import rest_framework.permissions
import rest_framework.response
import rest_framework.views
import rest_framework.viewsets

import posts.models
import posts.serializers


class PageNumberSetPagination(rest_framework.pagination.PageNumberPagination):
    page_size = 6
    page_size_query_param = "page_size"
    ordering = "created_at"


class PostViewSet(rest_framework.viewsets.ModelViewSet):
    search_fields = ["content", "h1"]
    filter_backends = (rest_framework.filters.SearchFilter,)
    serializer_class = posts.serializers.PostSerializer
    queryset = posts.models.Post.objects.all()
    lookup_field = posts.models.Post.slug.field.name
    permission_classes = [rest_framework.permissions.AllowAny]
    pagination_class = PageNumberSetPagination


class AsideView(rest_framework.generics.ListAPIView):
    queryset = posts.models.Post.objects.all().order_by("-id")[:5]
    serializer_class = posts.serializers.PostSerializer
    permission_classes = [rest_framework.permissions.AllowAny]


class FeedBackView(rest_framework.views.APIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    serializer_class = posts.serializers.ContactSerailizer

    def post(self, request, *args, **kwargs):
        serializer_class = posts.serializers.ContactSerailizer(
            data=request.data,
        )
        if serializer_class.is_valid():
            data = serializer_class.validated_data
            name = data.get("name")
            from_email = data.get("email")
            subject = data.get("subject")
            message = data.get("message")
            django.core.mail.send_mail(
                f"От {name} | {subject}",
                message,
                from_email,
                ["macalistervadim@yandex.ru"],
            )
            return rest_framework.response.Response({"success": "Sent"})

        return None


class RegisterView(rest_framework.generics.GenericAPIView):
    permission_classes = [rest_framework.permissions.AllowAny]
    serializer_class = posts.serializers.RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return rest_framework.response.Response(
            {
                "user": posts.serializers.UserSerializer(
                    user,
                    context=self.get_serializer_context(),
                ).data,
                "message": "Пользователь успешно создан",
            },
        )


class ProfileView:
    pass
