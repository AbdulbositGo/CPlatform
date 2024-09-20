from django.db import models



class AccessRequirement(models.TextChoices):
    Anyone = "any", "Anyone"
    EMAIL_REQUIRED = 'email_required', "Email Required"


class PublishStatus(models.TextChoices):
    PUBLISHED = "pub", "Published"
    COMING_SOON = 'soon', "Coming Soon"
    DRAFT = 'draft', 'Draft'


class Course(models.Model):
    title = models.CharField('Title', max_length=150)
    description = models.TextChoices(blank=True, null=True)
    acces = models.CharField(
        max_length=10,
        choices=AccessRequirement.choices,
        default=AccessRequirement.Anyone
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
    
    