from django.db import models
from common.models import BaseModel
from users.models import CustomUser
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType



class CATEGORY(models.TextChoices):
    HEALING = "healing", "healing"
    FINANCE = "finance", "finance"
    BREAKTHROUGH = "breakthrough", "breakthrough"
    PROTECTION = "protection", "protection"
    SALVATION = "salvation", "salvation"
    DELIVERANCE = "deliverance", "deliverance"
    RESTORATION = "restoration", "restoration"
    SPIRITUAL_GROWTH = "spiritual_growth", "spiritual growth"
    EDUCATION = "education", "education"
    CAREER = "career", "career"
    OTHER = "other", "other"
    
    
""" Base Testimony Class """

class Testimony(BaseModel):
    title = models.CharField(max_length=255, help_text="Enter title")
    category = models.CharField(max_length=50, choices=CATEGORY.choices)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rejection_reason = models.TextField(blank=True, null=True)
    likes = GenericRelation("Like")
    comments = GenericRelation("comment")
    shares = GenericRelation("Share")
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return f"Testimony by: {self.uploaded_by.full_name}"
    
class TextTestimony(Testimony):
    
    class STATUS(models.TextChoices):
        PENDING = "pending", "pending"
        APPROVED = 'approved', 'approved'
        REJECTED = 'rejected', 'rejected'
    
    content = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS.choices, default=STATUS.PENDING)
    
    
class SocialInteraction(BaseModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.UUIDField()
    content_object = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        abstract = True
        unique_together = ("content_type", "object_id", "user")
        
    def __str__(self):
        return f"{self.__class__.__name__} by {self.user.full_name}"
    
    
class Comment(SocialInteraction):
    text = models.TextField()
    

class Like(SocialInteraction):
    pass


class Share(SocialInteraction):
    pass
