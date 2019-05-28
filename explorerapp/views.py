from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

#from .models import
#from .forms import


from django.shortcuts import render

# Create your views here.

def index(request):
    #strona glowna
    return render(request, 'explorerapp/index.html')