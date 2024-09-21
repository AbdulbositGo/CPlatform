from django.contrib import admin
from django.utils.html import format_html
from cloudinary import CloudinaryImage

from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'description',
        'image',
        'display_image',
        'access',
        'status',
    ]
    list_filter = ['access', 'status']
    readonly_fields = ['display_image']
    
    def display_image(self, obj, *args, **kwargs):
        return format_html(obj.image_admin)

    display_image.short_description = "Current Image"