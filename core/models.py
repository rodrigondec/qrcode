import uuid

from django.db import models
from polymorphic import models as pmodels


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = models.Manager()

    class Meta:
        abstract = True


class BasePolymorphicModel(pmodels.PolymorphicModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    objects = pmodels.PolymorphicManager()

    class Meta:
        abstract = True
