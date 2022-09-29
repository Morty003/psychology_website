from django.shortcuts import render
from .models import Main_page_model

def main_page_view(request):
    main_page = Main_page_model.objects.all()
    return render(request, 'main_page/index.html', context={
        'main_page': main_page
    })
