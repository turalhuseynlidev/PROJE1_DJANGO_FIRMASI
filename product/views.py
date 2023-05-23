from django.shortcuts import render
from .fake_db.product import FAKE_DB_PRODUCTS
from django.http import Http404
# Create your views here.
def product_list_view(request):
    context = dict(
        products = FAKE_DB_PRODUCTS,
    )
    return render(request, 'product/products.html', context)

def product_detail_view(request, id):
    result = list(filter(lambda x: (x['id'] == id), FAKE_DB_PRODUCTS))
    if result:
        context = dict(
            products=FAKE_DB_PRODUCTS,
            item=result[0],
           
        )
        return render(request, 'product/product_detail.html', context)
    raise Http404