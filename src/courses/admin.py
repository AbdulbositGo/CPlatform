from django.contrib import admin
from django.utils.html import format_html
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
        url = obj.image.url
        return format_html(f'<img src="{url}" hight="30px" >')

    display_image.short_description = "Current Image"