from django.shortcuts import render

# Create your views here.
#views.py
from login.forms import *
from login.citation import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from login.models import *


# @csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
            )
            user.save()
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
    return render_to_response(
    'registration/register.html',
    variables,
    )

def register_success(request):
    return render_to_response(
    'registration/success.html',
    )

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    # if request.method=='GET':
    # obj = Citation.objects.all()

    return render_to_response('home.html',{ 'obj': Citation.objects.all() } )
    # if request.method =='POST':
    #     return render_to_response('home.html',{'user':'whatever'})

# @csrf_protect
def submitcitation(request):
    if request.method == 'POST':
        form =  CitationForm(request.POST)
        citation = Citation(
                title=form.clean['title'],
                notes=form.clean['notes'],
                link=form.clean['link'],
            )
        citation.save()
        return render_to_response('home.html', {'user': request.user})

    else:
        form = CitationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('AddCitation.html',variables)
