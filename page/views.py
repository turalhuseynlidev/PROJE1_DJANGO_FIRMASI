from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    # print(request.META)
    return HttpResponse('Ana sehifeye xos geldiniz...')