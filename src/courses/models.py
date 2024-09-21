from django.db import models
from cloudinary.models import CloudinaryField

import helpers


helpers.cloudinary_init()


class AccessRequirement(models.TextChoices):
    Anyone = "any", "Anyone"
    EMAIL_REQUIRED = 'email_required', "Email Required"


class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = 'soon', "Coming Soon"
    DRAFT = 'draft', 'Draft'

class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField('image', null=True)
    access = models.CharField(
        max_length=14,
        choices=AccessRequirement.choices,
        default=AccessRequirement.EMAIL_REQUIRED
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.DRAFT
    )
    
    def __str__(self):
        return f'{self.title[:15]} is {self.status}'
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
    
    @property
    def image_admin(self):
        if not self.image:
            return ''
        image_options = {
            'width': 200
        }
        url = self.image.image(**image_options)
        return url
        
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    thumbnail = CloudinaryField('image', blank=True, null=True)
    video = CloudinaryField('video', resource_type='video', blank=True, null=True)
    access = models.BooleanField(default=False, 
        help_text="Even if the user does not have access to the course,\
        can still access this lesson"
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
    )
    