from django.db import models

#Import User method for django
from django.contrib.auth.models import User
'''End Of Import'''
#---------------------------------------------------------------------#


# MODELS CREATED HERE!

#################################################################################################################################################################################
# MODEL FOR DRIVER(UBER)!
#################################################################################################################################################################################

#...Class DRIVER added here...
class Driver(models.Model):
#Attribute Variables for Driver class to represent different columns in database
    '''
    name-: This is the name of the driver 
    avatar-: A picture in the profile to show the rider how the driver looks like
    car-: This is the car that will be used to pick up the rider connected to Car class using a FOREIGN-KEY
    pickup_location-: Connected to the Location class using a FOREIGN_KEY
    '''
    name = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=60)
    avatar = models.ImageField(upload_to='ProfilePicture/')
    vehicle = models.ForeignKey('uber.Car', on_delete=models.CASCADE)
    pickup_location = models.ForeignKey('uber.Location', on_delete=models.CASCADE)
    contact_info = models.CharField(max_length=50)

    
    '''Method to filter database results'''
    def __str__(self):
        return self.user.username 

