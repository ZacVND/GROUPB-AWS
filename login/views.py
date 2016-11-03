from django.shortcuts import render, redirect

# Create your views here.
#views.py
from login.forms import *
from login.citation import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import UserManager
# from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from login.models import *
from login.userinfo import *


def login(request):
    if request.method == 'POST':
            form = Userinfo(request.POST)


            try:
                p = User.objects.get(username=form.username)

                if p == form.password:
                     return home

            except User.DoesNotExist:
                raise forms.ValidationError("User not exist.")

            #
            # if user is not None:
            #     return render(request, 'home.html', {'form': form})

    return render(request, 'registration/login.html', {'form': form})

# @csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # userManager =
            # user = User(userManager, username=form.cleaned_data['username'],
            #                                 email=form.cleaned_data['email'],
            #                                password=form.cleaned_data['password'],)

            user = User(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email'],
            )
            user.save()
            return redirect('/register/success')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render(request, 'registration/register.html', {'form': form})

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
    # return render_to_response('AddCitation.html',variables)
    return render(request, 'AddCitation.html', {'form': form})