from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length= 100, null=False )
    id = models.IntegerField()
    reg_date = models.DateField(max_length =100 )
    course = models.CharField(max_length= 100)

    def __str__(self):
        return self.title
