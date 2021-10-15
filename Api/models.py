from django.db import models

# Create your models here.
class People(models.Model):
    name=  models.CharField(max_length=200, unique=True)       
    height = models.CharField(max_length=200)
    mass = models.CharField(max_length=200)
    hair_color =  models.CharField(max_length=200)
    skin_color =  models.CharField(max_length=200)
    eye_color =  models.CharField(max_length=200)
    birth_year = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    homeworld = models.CharField(max_length=200,default="non")
 
# {
#     "name":"Sarah",      
#     "height":"150",
#     "mass":"50kg",
#     "hair_color":"brown",
#     "skin_color":" brown",
#     "eye_color":"brown",
#     "birth_year":"1996",
#     "gender":"female"
# }