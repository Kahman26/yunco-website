from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Tariff, Project, Review, ProjectImage


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('title','description')


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1
    max_num = 15
    fields = ('image_preview', 'image', 'order', 'created_at')
    readonly_fields = ('created_at', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="height:60px;border-radius:4px;">')
        return "(нет)"
    image_preview.short_description = "Превью"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at', 'cover_image_preview')
    list_editable = ('order',)
    search_fields = ('title', 'description')
    inlines = [ProjectImageInline]

    def cover_image_preview(self, obj):
        url = obj.cover_image
        if url:
            return mark_safe(f'<img src="{url}" style="height:60px;border-radius:4px;">')
        return "(нет обложки)"
    cover_image_preview.short_description = "Обложка"


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'order', 'created_at')
    list_editable = ('order',)
    search_fields = ('author','text')