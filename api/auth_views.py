from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from . import  serializer
from base import  google


def google_login(request):

    return render(request, 'api/google_login.html')



@api_view(['POST'])
def google_auth(request):
    """ Confirm authentical for Google"""
    google_data = serializer.GoogleAuth(data=request.data)
    if google_data.is_valid():
       token = google.check_google_auth(google_data.data)
       return Response(token)
    else:
        return AuthenticationFailed(cod=403, detail='Bed data Google')