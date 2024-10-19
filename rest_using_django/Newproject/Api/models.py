from django.db import models

# Create your models here.
class User(models.Model):
    Name = models.CharField(max_length=300)
    Age = models.IntegerField()
    
    
    def __str__(self):
        return self.Name
    
    
    