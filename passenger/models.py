from django.db import models
from uber.models import Location

#Import User method for django
from django.contrib.auth.models import User
'''End Of Import'''
#---------------------------------------------------------------------#



# MODELS CREATED HERE!

#################################################################################################################################################################################
# MODEL FOR PASSENGERS!
#################################################################################################################################################################################

#...Class DRIVER added here...
class Passenger(models.Model):
#Attribute Variables for Driver class to represent different columns in database
    '''
    name-: This is the name of the passenger
    avatar-: A picture of the rider
    pickup_location-: Connected to the Location class using a FOREIGN_KEY
    '''
