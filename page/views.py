from django.shortcuts import render
from django.http import HttpResponse
from random import randint

FAKE_DB_PROJECTS = [
    f"https://picsum.photos/id/{id}/100/80" for id in range(21, 29)
]
FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/500" for id in range(41, 45)
]





# Create your views here.
def home_view(request):
    # print(request.META)
    context = dict(
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS,
        FAKE_DB_CAROUSEL=FAKE_DB_CAROUSEL,
    )
    return render(request, "page/home_page.html", context)

def about_us_view(request):
    hero_content = "Or, keep it light and add a border for some added definition to theboundaries of your content. Be sure to look under the hood at the source HTML here as we'veadjusted the alignment and sizing of both column's content for equal-height."
    page_title = 'Hakkimizda'
    # print(request.META)
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS
    )
    return render(request, "page/about_us.html", context)

def vision_view(request):
    # print(request.META)
    page_title = 'Vizyonumuz'
    hero_content = "Or, keep it light and add a border for some added definition to theboundaries of your content. Be sure to look under the hood at the source HTML here as we'veadjusted the alignment and sizing of both column's content for equal-height."
    # print(request.META)

    # dictionary bele de yigila biler: 

    context = {
    "page_title":page_title,
    "hero_content":hero_content,
    "FAKE_DB_PROJECTS":FAKE_DB_PROJECTS
    }
    return render(request, "page/vision.html", context)

def contact_us_view(request):
    # print(request.META)
    page_title = 'Iletisim'
    hero_title = 'Contact with us'
    hero_content = "Or, keep it light and add a border for some added definition to theboundaries of your content. Be sure to look under the hood at the source HTML here as we'veadjusted the alignment and sizing of both column's content for equal-height."
    # print(request.META)
    context = dict(
        page_title=page_title,
        hero_content = hero_content,
        FAKE_DB_PROJECTS=FAKE_DB_PROJECTS
    )
    return render(request, "page/contact_us.html", context)

def test_page(request):
    # print(request.META)
    page_title = 'Test Page'
    hero_title = ''
    # print(request.META)
    context = dict(
        page_title=page_title,
    )
    return render(request, "page/test_page.html", context)

def agamirli(request):
    # print(request.META)
    # print(request.META)
    return render(request, "page/agamir_agamirli.html")
def tural(request):
    # print(request.META)
    # print(request.META)
    return render(request, "page/tural_huseynli.html")