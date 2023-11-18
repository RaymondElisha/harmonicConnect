from .utils import match_clients_to_service_providers
from .models import UserProfile, Client, Event, EntertainmentServiceProvider
from .forms import EventForm
from django.shortcuts import render, get_object_or_404
from .models import UserProfile, Client, Event
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

# core/views.py

from django.shortcuts import render

def index(request):
    # Your view logic here
    return render(request, 'index.html')  # or the appropriate template

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Automatically log in the user after registration
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the home page or any other desired page
                return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to the home page or any other desired page
                return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    # Redirect to the home page or any other desired page
    return redirect('home')


@login_required
def user_profile(request):
    # Retrieve or create the user's profile
    user_profile, created = UserProfile.objects.get_or_create(
        user=request.user)

    # Display user profile details
    return render(request, 'profile.html', {'user_profile': user_profile})


@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save()
            # Create the event for the current user
            client = get_object_or_404(Client, user_profile__user=request.user)
            event = Event.objects.create(
                client=client,
                event_type=form.cleaned_data['event_type'],
                location=form.cleaned_data['location'],
                genres=form.cleaned_data['genres'],
                date=form.cleaned_data['date']
                # Add other event details
            )
            return redirect('event', event_id=event.id)

    else:
        form = EventForm()

    # Render the event creation form
    return render(request, 'create_event.html', {'form': form})

def event(request, event_id):
    event = Event.objects.get(pk=event_id)
    return render(request, 'event.html', {'event': event})