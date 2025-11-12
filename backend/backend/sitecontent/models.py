from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError


class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0, help_text='Порядок вывода (меньше = выше)')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title

    def as_dict(self, request=None):
        # Возвращает словарь пригодный для JSON
        image_url = None
        if self.image:
            image_url = self.image.url
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_url": image_url,
        }


class Tariff(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.CharField(max_length=100, blank=True, help_text='Отображаемая цена, строка (например: ¥500)')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Тариф"
        verbose_name_plural = "Тарифы"

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "price": self.price,
        }


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"

    def __str__(self):
        return self.title

    @property
    def cover_image(self):
        first_image = self.projectimage_set.order_by('order', 'id').first()
        return first_image.image.url if first_image and first_image.image else None

    def as_dict(self):
        images = []
        imgs = self.projectimage_set.all().order_by('order', 'id')
        for img in imgs:
            if img.image:
                images.append(img.image.url)

        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "image_url": self.cover_image,
            "images": images,
        }


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/')
    order = models.PositiveIntegerField(default=0, help_text='0 — обложка карточки')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', 'id']
        verbose_name = "Фото проекта"
        verbose_name_plural = "Фотографии проектов"

    def __str__(self):
        name = self.image.name if self.image else "Без изображения"
        return f"{self.project.title if self.project_id else '(новый проект)'} — {name}"


class Review(models.Model):
    author = models.CharField(max_length=200)
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.author}"

