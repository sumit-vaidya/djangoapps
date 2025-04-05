from django.db import models

# Create your models here.
class Emp(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=20)
    sal=models.FloatField()
    sex=models.CharField(max_length=6)
    dno=models.IntegerField()
    def __str__(self):
        return self.ename