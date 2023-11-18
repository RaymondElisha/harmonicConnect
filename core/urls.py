from . import views
from .views import event, user_profile, create_event
from django.urls import path
from .views import user_register, user_login, user_logout, index

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', user_profile, name='user_profile'),
    path('create_event/', create_event, name='create_event'),
    path('create_event/', create_event, name='create_event'),
    path('event/<int:event_id>/', event, name='event'),
    # Add other URL patterns as needed
]
