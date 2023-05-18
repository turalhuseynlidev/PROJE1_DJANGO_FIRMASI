from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    # print(request.META)
    context = dict()
    return render(request, "page/home_page.html", context)

def about_us_view(request):
    page_title = 'Hakkimizda'
    # print(request.META)
    context = dict(
        page_title=page_title,
    )
    return render(request, "page/about_us.html", context)

def vision_view(request):
    # print(request.META)
    page_title = 'Vizyonumuz'
    # print(request.META)
    context = dict(
    page_title=page_title,
    )
    return render(request, "page/vision.html", context)

def contact_us_view(request):
    # print(request.META)
    page_title = 'Iletisim'
    # print(request.META)
    context = dict(
        page_title=page_title,
    )
    return render(request, "page/contact_us.html", context)

def test_page(request):
    # print(request.META)
    page_title = 'Test Page'
    # print(request.META)
    context = dict(
        page_title=page_title,
    )
    return render(request, "page/test_page.html", context)