import django.contrib.auth.models
import django.db
import django.utils.translation as translation


class UserProfile(django.db.models.Model):
    """
    Профиль пользователя
    """

    user = django.db.models.OneToOneField(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
    )
    birthday = django.db.models.DateField(
        translation.gettext_lazy("дата рождения"),
        null=True,
        blank=True,
        help_text=translation.gettext_lazy(
            "Выберите дату своего рождения",
        ),
    )

    class Meta:
        verbose_name = translation.gettext_lazy("профиль пользователя")
        verbose_name_plural = translation.gettext_lazy(
            "профили пользователей",
        )

        ordering = ("user",)

    def __str__(self):
        return f"Профиль пользователя {self.user.username[:25]}"
    