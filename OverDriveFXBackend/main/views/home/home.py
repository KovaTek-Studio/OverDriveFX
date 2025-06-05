from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome Home OverDriveFX</h1><br>Can you center this div? xd")

@login_required
def login(request):
    print("")