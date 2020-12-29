from django.db import models


# Create your models here.

class Contacts(models.Model):
    class Meta:
        verbose_name_plural = "about"

    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
   
    number = models.CharField(max_length=12)
    
    def __str__(self):
        return self.name
    
 



    