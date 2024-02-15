from django.shortcuts import render

# Create your views here.
def index(request):
    '''Render the index.html template'''
    return render(request, 'users/index.html')

def map(request):
    '''Render the map.html template'''
    return render(request, 'users/map.html')