from django.db import models

class ProgramaTV(models.Model):
    id = models.IntegerField(primary_key=True)
    nameprogram = models.CharField(max_length=60)
    synopsis = models.CharField(max_length=60)
    agegroup = models.IntegerField(default=0)
    host = models.CharField(max_length=60)
    time = models.CharField(max_length=60)
    broadcaster = models.CharField(max_length=60)
    def __str__(self):
        return self.nameprogram