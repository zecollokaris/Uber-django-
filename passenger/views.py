from django.shortcuts import render

from django.http import HttpResponse
'''End Of Import'''
#---------------------------------------------------------------------#


# VIEW FUNCTIONS HERE!

#################################################################################################################################################################################
#LANDING PAGE VIEW FUNCTION
#################################################################################################################################################################################

#Login page view function
def landing(request):
    return render(request, 'landingpage/land-page.html')

