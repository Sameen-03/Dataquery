from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def data_analyst(request):
    return render(request, 'data_analyst.html')

def roadmaps(request):
    return render(request, 'roadmaps.html')

def courses(request):
    return render(request, 'courses.html')

def books(request):
    return render(request, 'books.html')

