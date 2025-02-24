from django.db import models

class GetOrNoneQuerySet(models.QuerySet):
    """Custom Queryset that supports get_or_none()"""

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None