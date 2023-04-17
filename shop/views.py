from django.shortcuts import render
from .models import Products, Order
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    """
    Renders the index page of the shop app, displaying a paginated 
    list of all products available in the database, or a filtered 
    list of products if a search query is provided.

    :param request: The HTTP request object.
    :return: The rendered index page with the list of product objects.
    """
    # Retrieve all product objects from the database
    product_objects = Products.objects.all()
    
    # Search code
    # If a search query is provided, filter the product objects to show only those that match the query
    item_name = request.GET.get('item_name')
    if item_name != '' and item_name is not None:
        product_objects = product_objects.filter(title__icontains=item_name)

    # Paginator code
    # Paginate the product objects to show only a certain number of products per page
    paginator = Paginator(product_objects, 4)
    page = request.GET.get('page')
    product_objects = paginator.get_page(page)
    
    # Render the index page and pass the product objects to the template
    return render(request, 'shop/index.html', {'product_objects': product_objects})


def detail(request, id):
    """
    Renders the detail page for a specific product, identified by the provided ID.

    :param request: The HTTP request object.
    :param id: The ID of the product to display.
    :return: The rendered detail page with the product object.
    """
    product_object = Products.objects.get(id=id)
    return render(request,'shop/detail.html',{'product_object':product_object})


def checkout(request):
    """
    Renders the checkout page, and saves an order object to the database if the form is submitted.

    :param request: The HTTP request object.
    :return: The rendered checkout page.
    """
    if request.method == "POST":
        items = request.POST.get('items','')
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state = request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        total = request.POST.get('total',"")
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode,total=total)
        order.save()
    return render(request, 'shop/checkout.html')
