from django.shortcuts import render
from .models import Gallery

def about_view(request):
    gallery = Gallery.objects.all()
    return render(request, 'about/about.html', context={
        'gallery': gallery
    })
