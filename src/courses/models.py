from django.db import models
from cloudinary.models import CloudinaryField

import helpers


helpers.cloudinary_init()


def handle_upload(instance, filename):
    return filename

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
    
    