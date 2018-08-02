from django.conf.urls import url
from django.urls import include, path
from .import views
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
'''End Of Import'''
#---------------------------------------------------------------------#


urlpatterns=[
#################################################################################################################################################################################
#URL FOR  LANDING-PAGE
#################################################################################################################################################################################

    #LANDING Page url!
    
    #This is the landing-page url pattern having the ( ^ )-sign at the start means nothing comes before the defined url which will make it the index page##
    
    path('^$',views.landing,name = 'landing'),

#################################################################################################################################################################################
#URL FOR  PASSENGER'S HOME-PAGE
#################################################################################################################################################################################

    #PASSENGER'S HOME-PAGE url!
    
    #This is the home-page url for passenger
    
    path('passenger/home',views.passenger, name = 'passenger home page'),

#################################################################################################################################################################################
#URL FOR   PASSENGER'S PROFILE-PAGE
#################################################################################################################################################################################

    #PASSENGER'S PROFILE-PAGE url!
    
    path('passenger/profile',views.pprofile, name = 'passenger profile page'),


]