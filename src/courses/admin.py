from django.contrib import admin
from django.utils.html import format_html
from cloudinary import CloudinaryImage

import helpers
from .models import Course, Lesson


class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 0
    readonly_fields = ['display_image', 'display_video', 'public_id', 'updated', 'created']
    
    def display_image(self, obj, *args, **kwargs):
        return format_html(
            helpers.get_cloudinary_image(
                obj,
                as_html=True,
                field_name='thumbnail'
            )
        )
    display_image.short_description = "Current Image"
    
    def display_video(self, obj, *args, **kwargs):
        return format_html(
            helpers.get_cloudinary_video(
                obj,
                as_html=True,
                width=500,
            )
        )
    display_video.short_description = "Current Video"


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    fields = [
        'public_id',
        'title',
        'description',
        'image',
        'display_image',
        'access',
        'status',
        'created',
        'updated'
    ]
    inlines = [LessonInline]
    list_filter = ['access', 'status']
    readonly_fields = ['public_id', 'display_image', 'created', 'updated']
    
    def display_image(self, obj, *args, **kwargs):
        return format_html(
            helpers.get_cloudinary_image(
                obj,
                as_html=True,
            )
        )

    display_image.short_description = "Current Image"