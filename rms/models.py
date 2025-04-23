from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
     return self.name
 
class Food(models.Model):
     name = models.CharField(max_length=225)
     price = models.IntegerField()
     Category = models.ForeignKey(Category,on_delete=models.CASCADE)
     
     def __str__(self):
         return self.name
     