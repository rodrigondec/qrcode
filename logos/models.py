from django.db import models

from core.models import BaseModel
from logos.utils import get_img_path


class Logo(BaseModel):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to=get_img_path)

    class Meta:
        ordering = ('id',)