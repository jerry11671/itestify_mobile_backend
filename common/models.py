from django.db import models 
from .managers import GetOrNoneManager
import uuid 

class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    created_at = models.DateTimeField("Date Created" ,auto_now_add=True, null=True)
    updated_at = models.DateTimeField("Date Updated", auto_now=True, null=True)

    objects = GetOrNoneManager()

    class Meta:
        abstract = True
