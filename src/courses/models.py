from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
import uuid

import helpers


helpers.cloudinary_init()


class AccessRequirement(models.TextChoices):
    Anyone = "any", "Anyone"
    EMAIL_REQUIRED = 'email_required', "Email Required"


class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = 'soon', "Coming Soon"
    DRAFT = 'draft', 'Draft'


def generate_public_id(instalce, *args, **kwargs):
    title = instalce.title
    unique_id = str(uuid.uuid4()).replace('-', '')
    if not title:
        return unique_id
    slug = slugify(title)
    unique_id_short = unique_id[:5]
    return f"{slug}-{unique_id_short}"

def get_public_id_prefix(instance, *args, **kwargs):
    public_id = instance.public_id
    if not public_id:
        return 'courses'
    return f'courses/{public_id}'
        
    
    return "courses"

def get_display_name(instance, *args, **kwargs):
    title = instance.title
    if title:
        return title
    return "Course Upload"
        


class Course(models.Model):
    title = models.CharField(max_length=150)
    public_id = models.CharField(max_length=160, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = CloudinaryField(
        'image',
        public_id_prefix=get_public_id_prefix,
        display_name=get_display_name,
        tags=['course', 'thumbnail'],
        null=True,
        blank=True
    )
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
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title[:15]} is {self.status}'
    
    def save(self, *args, **kwargs):
        if self.public_id == '' or self.public_id is None:
            self.public_id = generate_public_id(self)
        super(*args, **kwargs).save()
    
    @property
    def is_published(self):
        return self.status == PublishStatus.PUBLISHED
       
    
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    public_id = models.CharField(max_length=160, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    thumbnail = CloudinaryField(
        'image',
        public_id_prefix=get_public_id_prefix,
        display_name=get_display_name,
        tags=['lesson', 'thumbnail'], 
        blank=True, 
        null=True
    )
    video = CloudinaryField(
        'video', 
        resource_type='video', 
        public_id_prefix=get_public_id_prefix,
        display_name=get_display_name,
        tags=['lesson', 'video'],
        type="private",
        blank=True, 
        null=True
    )
    order = models.SmallIntegerField(default=0)
    access = models.BooleanField(default=False, 
        help_text="Even if the user does not have access to the course,\
        can still access this lesson"
    )
    status = models.CharField(
        max_length=10,
        choices=PublishStatus.choices,
        default=PublishStatus.PUBLISHED
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order', '-updated']
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if self.public_id == '' or self.public_id is None:
            self.public_id = generate_public_id(self)
        super(*args, **kwargs).save()   