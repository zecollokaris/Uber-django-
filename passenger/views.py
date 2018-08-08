from django.shortcuts import render, redirect

from django.conf import settings

from django.http import HttpResponse

from django.conf.urls.static import static

from . import models

from django.contrib.auth.models import User


from django.contrib.auth.decorators import login_required
'''
The @login_required declarator limits access of view function to only 
authenticated users
'''
#---------------------------------------------------------------------#
'''End Of Import'''
#---------------------------------------------------------------------#

# VIEW FUNCTIONS HERE!


#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Login page view function
def landing(request):
    return render(request, 'landingpage/land-page.html')


#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S PROFILE-PAGE
#################################################################################################################################################################################

#PASSENGER'S PROFILE-PAGE view function

'''
 This page contains passengers info eg Name, Bio and useful information about driver
'''
@login_required(login_url="/accounts/login/")
def pprofile(request):
    return render(request, 'passenger/profile.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S  DESTINATION-PAGE
#################################################################################################################################################################################

#PASSENGER'S  DESTINATION-PAGE view function

'''
 This page enables passenger pick a destination point where they can be droped off
'''
@login_required(login_url='/accounts/login/')
def pdestination(request):
    return render(request, 'passenger/destination.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  PASSENGER'S  CONTACT-PAGE
#################################################################################################################################################################################

#PASSENGER'S  DESTINATION-PAGE view function

'''
 This page gives passenger contact info
'''
@login_required(login_url='/accounts/login/')
def pcontact(request):
    return render(request, 'passenger/contact.html')

#################################################################################################################################################################################
#VIEW FUNCTION FOR  ABOUT-PAGE
#################################################################################################################################################################################

#ABOUT-INFO-PAGE

'''
 This page basically explains what the app is about
'''
@login_required(login_url='/accounts/login/')
def about(request):
    return render(request, 'uber/about.html')

#################################################################################################################################################################################
#LOGIN PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Login page view function
def login(request):
    return render(request, 'registration/login.html')

#################################################################################################################################################################################
#LOGOUT PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Logout page view function
def logout(request):
        logout(request)
        return redirect(request, 'registration/logout.html')

#################################################################################################################################################################################
#################################################################################################################################################################################