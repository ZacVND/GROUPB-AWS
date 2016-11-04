from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.http import JsonResponse
from django.core.exceptions import *
from login.models import User, Citation

import json

def register(request):
    if request.method == 'POST':

        post_obj = dict(request.POST)

        username = post_obj['username'][0]

        email = post_obj['email'][0]

        password = post_obj['password'][0]

        user = User(
            username=username,
            email=email,
            password=password,
        )

        user.save()

        return redirect('/')

    else:
        return render(request, 'registration/register.html')


def login(request):
    if request.method != 'POST':
        return render(request, 'registration/login.html')

    post_obj = dict(request.POST)

    try:
        user =  User.objects.get(username=post_obj['username'][0], password=post_obj['password'][0])

    except ObjectDoesNotExist:
        return redirect('/register')

    except MultipleObjectsReturned:
        user = User.objects.filter(username=post_obj['username'][0], password=post_obj['password'][0]).first()

    try:
        citations = list(Citation.objects.all().values())

        return render(request, 'main.html', {'user': user, 'citations': json.dumps(citations)})

    except ObjectDoesNotExist:
        return render(request, 'main.html', {'citations': 'None exists'})


def add_citation(request):
    if request.method != 'POST':
        return JsonResponse({'success': 0})

    post_obj = dict(request.POST)

    content_text = post_obj['content'][0]

    try:
        cit = Citation(content=content_text)
        cit.save()
        return JsonResponse({'success': 1})

    except (FieldError, FieldDoesNotExist) as e:
        return JsonResponse({'success': 0})


def delete_citation(request):
    if request.method != 'POST':
        return JsonResponse({'success': 0})

    post_obj = dict(request.POST)

    unique_id = post_obj['id'][0]

    content = post_obj['content'][0]

    try:
        Citation.objects.filter(id=unique_id, content=content).delete()
        return JsonResponse({'success': 1})

    except:
        return JsonResponse({'success': 1})


def register_success(request):
    return render(request, 'registration/success.html')



def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
