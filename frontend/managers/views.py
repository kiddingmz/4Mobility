from django.shortcuts import render


# Create your views here.
def index(request):
    '''Render the index.html template'''
    return render(request, 'managers/pages/index.html', {'name': 'Dashboard'})


def map(request):
    '''Render the map.html template'''
    return render(request, 'managers/pages/map.html', {'name': 'Map'})
