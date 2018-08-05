from django.shortcuts import render

from django.http import HttpResponse
from django.conf.urls import url,include

'''End Of Import'''
#---------------------------------------------------------------------#


# VIEW FUNCTIONS HERE!



#################################################################################################################################################################################
#LOGIN PAGE VIEW FUNCTION
#################################################################################################################################################################################

#LOGIN Page View Function!
def login(request):
    return render(request, "registration/registration_form.html")
    
