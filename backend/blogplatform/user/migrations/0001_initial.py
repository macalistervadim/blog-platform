# Generated by Django 5.0.6 on 2024-06-28 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "birthday",
                    models.DateField(
                        blank=True,
                        help_text="Выберите дату своего рождения",
                        null=True,
                        verbose_name="дата рождения",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "профиль пользователя",
                "verbose_name_plural": "профили пользователей",
                "ordering": ("user",),
            },
        ),
    ]
