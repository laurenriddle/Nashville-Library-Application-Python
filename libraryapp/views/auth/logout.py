from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
# this function logs the user out and redirects them to the login page
def logout_user(request):
    logout(request)
    return redirect(reverse('libraryapp:login'))