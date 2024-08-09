#from django.db import models
from django.db import models
#from django.contrib.gis.geos import GEOSGeometry
#A.geoCoords = GEOSGeometry('POINT(LON LAT)', srid=4326)
# Create your models here.
class SensorData(models.Model):
    id = models.AutoField(primary_key=True)
    time = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    pres = models.FloatField(blank=True, null=True)
    depth = models.FloatField(blank=True, null=True)
    temp = models.FloatField(blank=True, null=True)
    psal = models.FloatField(blank=True, null=True)
    dox1 = models.FloatField(blank=True, null=True)
    dox2 = models.FloatField(blank=True, null=True)
    cphl = models.FloatField(blank=True, null=True)
    cdom = models.FloatField(blank=True, null=True)
    cndc = models.FloatField(blank=True, null=True)
    vbsc = models.FloatField(blank=True, null=True)
    head = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sensor_data'
        unique_together = (('time', 'latitude'),)