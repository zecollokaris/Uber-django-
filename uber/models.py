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

#################################################################################################################################################################################
# MODEL CAR WHICH IS THE DRIVER'S CAR INFO!
#################################################################################################################################################################################

#...Class CAR added here...
class Car(models.Model):
#Attribute Variables for Car class to represent different columns in database
    '''
    car_brand -: This is the car brand driven by driver for easy identification 
    number_plate-: Vehicle registration number for more accurate identification
    seat_number-: This are the number of seats available in drivers car
    '''
    car_brand = models.CharField(max_length=50)
    number_plate = models.CharField(max_length=20)
    seat_number = models.CharField(max_length=20)


    '''Method to filter database results'''
    def __str__(self):
        return self.user.username 

#################################################################################################################################################################################
# MODEL LOCATION WHICH IS USED FOR DISPLAYING LOCATIONS EITHER (PICKUP/ DESTINATIONS)!
#################################################################################################################################################################################

#...Class LOCATION added here...
class Location (models.Model):
#Attribute Variables for Location class to represent different columns in database

    ''' 
    location_name-: This is the name of the point selected by the longitude & latitude
    category-: This is linked to category class to enable passenger know if it is pickup location or destination
    '''
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    location_name = models.CharField(max_length=20)
    category = models.ForeignKey('uber.Category', on_delete=models.CASCADE)

#################################################################################################################################################################################
# MODEL CATEGORY WHICH IS USED FOR ENABLING PASSENGERS KNOW IF IT IS (PICKUP/ DESTINATIONS)!
#################################################################################################################################################################################

#...Class CATEGORY added here...
class Category (models.Model):
#Attribute Variables for Category class to represent different columns in database

    ''' 
    pickup_location-: This is the location where user will be picked up
    arrival_destination-: This is the destination point where the driver will drop off passengers
    '''
    pickup_location = models.CharField(max_length=20)
    arrival_destination = models.CharField(max_length=20)

#################################################################################################################################################################################
