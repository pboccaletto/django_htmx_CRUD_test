from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404
from . import models
from . import forms

def index(request):
    users = models.UserProfile.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'core/index.html', context)

def index_create(request):
    # post is triggered when the form is submitted
    if request.method == 'POST':
        form = forms.UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        # GET request, initialize an empty form and returns it rendered in a modal
        form = forms.UserProfileForm()
    context = {
        'form': form,
    }
    return render(request, 'core/index_create.html', context)

def index_read(request):
    """Render the index read page."""
    if request.method == 'GET' and request.GET.get('id'):
        user = models.UserProfile.objects.get(id=request.GET.get('id'))
        context = {
            'user': user,
        }
        return render(request, 'core/index_read.html', context)
    return HttpResponse("User ID not provided", status=400)

                  
def index_update(request):
    if request.method == 'POST':
        user_id = request.POST.get('id')
        if not user_id:
            return HttpResponseBadRequest("Missing id")

        user = get_object_or_404(models.UserProfile, pk=user_id)
        print(f"Updating user: {user.name} {user.surename}")
        form = forms.UserProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, 'core/index_update.html', {'user': user, 'form': form})

    # GET
    user_id = request.GET.get('id')
    if not user_id:
        return HttpResponseBadRequest("Missing id")
    user = get_object_or_404(models.UserProfile, pk=user_id)
    form = forms.UserProfileForm(instance=user)
    return render(request, 'core/index_update.html', {'user': user, 'form': form})

def index_delete(request):
    """Render the index delete page."""
    if request.method == 'POST' and request.POST.get('id'):
        user_id = request.POST.get('id')
        user = models.UserProfile.objects.get(id=user_id)
        user.delete()
        return redirect('index')
    elif request.method == 'GET' and request.GET.get('id'):
        user_id = request.GET.get('id')
        user = models.UserProfile.objects.get(id=user_id)
        context = {
            'user': user,
        }
        return render(request, 'core/index_delete.html', context)
    return HttpResponse("Invalid request", status=400)