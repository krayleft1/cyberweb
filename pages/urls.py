from django.urls import path

from .views import HomePageView, FilePage
from .views import HomePage


urlpatterns = [
    path('myaccount/', HomePageView.as_view(), name='my_account'),
    path('', HomePage.as_view(), name='home'),
    path('files/', FilePage.as_view(), name='filepage'),
]