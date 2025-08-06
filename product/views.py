from django.shortcuts import render
from .models import MainContent

def index(request):
    comtent_list = MainContent.objects.order_by('-pub_date')
    context = {'comtent_list': comtent_list}
    return render(request,'product/content_list.html', context)