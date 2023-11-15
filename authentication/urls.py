from django.urls import path
from authentication.views import login
from main.views import logout_user

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_user, name='logout'),
]