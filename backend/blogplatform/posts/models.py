import ckeditor_uploader.fields
import django.contrib.auth.models
import django.db
import django.utils
import taggit.managers


class Post(django.db.models.Model):
    h1 = django.db.models.CharField(max_length=200)
    title = django.db.models.CharField(max_length=200)
    slug = django.db.models.SlugField()
    description = ckeditor_uploader.fields.RichTextUploadingField()
    content = ckeditor_uploader.fields.RichTextUploadingField()
    image = django.db.models.ImageField()
    created_at = django.db.models.DateField(default=django.utils.timezone.now)
    author = django.db.models.ForeignKey(
        django.contrib.auth.models.User,
        on_delete=django.db.models.CASCADE,
    )
    tags = taggit.managers.TaggableManager()

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"

        ordering = ("created_at",)

    def __str__(self):
        return f"Запись от {self.created_at}"
