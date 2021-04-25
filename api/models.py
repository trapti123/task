from django.db import models

# Create your models here.
class Student(models.Model):
    id=models.IntegerField(primary_key=True,blank=False,null=False)
    name=models.CharField(max_length=30,blank=False,null=False)
    age=models.IntegerField(blank=False,null=False)
    section=models.CharField(max_length=1, blank=False,null=False)

    
    def __str__(self):
        return self.name
