from django.shortcuts import render, redirect

# Create your views here.

def home_view(request):
    return render(request, "partidas/home.html")

#CRUD SISTEMAS

# List
# Detail
# Update
# Create 
# Delete