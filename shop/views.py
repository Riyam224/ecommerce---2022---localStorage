from math import prod
from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
# Create your views here.

from .models import Product , Order

def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        products = Product.objects.filter(title__icontains=item_name)
    #Paginator code & link 
    #https://docs.djangoproject.com/en/3.2/topics/pagination/
    paginator = Paginator(products,2)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    context  = {
        'products': products
    }

    return render(request , 'index.html',  context)


def detail(request , slug):
    product = get_object_or_404(Product , slug=slug)
    context = {
        'product': product
    }
    return render(request , 'detail.html' , context)


def checkout(request):

    if request.method == 'POST':

        items =request.POST.get('items',"") #allow the null value thats why put the empty string ""
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total','')

        order_list = Order( items = items,name = name, email = email, address = address, city = city, state = state, zipcode = zipcode,total = total)
        order_list.save()

   

    return render(request,'checkout.html')



def about(request):
    return render(request , 'about.html', {})