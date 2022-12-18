from django.shortcuts import render
from accounts.models import CustomUser


def index(request):
    users = CustomUser.objects.all()
    return render(request, "pages/my_account.html", {"users": users})
