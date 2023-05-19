from django.shortcuts import render



def home_page(request):
    """The main page of this app."""
    return render(request, "home_page.html")
