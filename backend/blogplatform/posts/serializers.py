import django.contrib.auth.models
import rest_framework
import taggit_serializer.serializers

import posts.models


class PostSerializer(
    taggit_serializer.serializers.TaggitSerializer,
    rest_framework.serializers.ModelSerializer,
):

    tags = taggit_serializer.serializers.TagListSerializerField()
    author = rest_framework.serializers.SlugRelatedField(
        slug_field="username",
        queryset=django.contrib.auth.models.User.objects.all(),
    )

    class Meta:
        model = posts.models.Post
        fields = "__all__"
        lookup_field = posts.models.Post.slug.field.name
        extra_kwargs = {
            "url": {"lookup_field": posts.models.Post.slug.field.name},
        }


class ContactSerailizer(rest_framework.serializers.Serializer):
    name = rest_framework.serializers.CharField()
    email = rest_framework.serializers.CharField()
    subject = rest_framework.serializers.CharField()
    message = rest_framework.serializers.CharField()


class RegisterSerializer(rest_framework.serializers.ModelSerializer):

    password2 = rest_framework.serializers.CharField(write_only=True)

    class Meta:
        model = django.contrib.auth.models.User
        fields = [
            "username",
            "password",
            "password2",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        password2 = validated_data["password2"]
        if password != password2:
            raise rest_framework.serializers.ValidationError(
                {"password": "Пароли не совпадают"},
            )

        user = django.contrib.auth.models.User(username=username)
        user.set_password(password)
        user.save()
        return user


class UserSerializer(rest_framework.serializers.ModelSerializer):
    class Meta:
        model = django.contrib.auth.models.User
        fields = "__all__"
