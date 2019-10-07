from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models

SRID_WGS84 = 4326


class PointModelMixin(models.Model):
    latitude = models.FloatField(validators=[MinValueValidator(-90), MaxValueValidator(90)],
                                 blank=True, null=True, verbose_name='Latitude')
    longitude = models.FloatField(validators=[MinValueValidator(-180), MaxValueValidator(180)],
                                  blank=True, null=True, verbose_name='Longitude')
    point = models.PointField(srid=SRID_WGS84, null=True, blank=True, verbose_name='Ponto')

    def save(self, *args, **kwargs):
        if self.latitude and self.longitude:
            self.latitude = float(self.latitude)
            self.longitude = float(self.longitude)
            self.point = Point(x=self.longitude, y=self.latitude, srid=SRID_WGS84)
        super(PointModelMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True

    @property
    def coordinates(self):
        return [self.latitude, self.longitude]
