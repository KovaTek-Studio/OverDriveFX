from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome Home OverDriveFX</h1><br>Can you center this div? xd")