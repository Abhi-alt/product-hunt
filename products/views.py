from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Product
from django.contrib import messages
# Create your views here.


def home(request):
    product = Product.objects.all
    return render(request, 'products/home.html', {'product': product})

@login_required
def create(request):
    if request.method == 'POST':

        title = request.POST['title']
        body = request.POST['body']
        icon = request.FILES['icon']
        image = request.FILES['image']
        url = request.POST['url']
        if url.startswith("https://") or url.startswith("http://"):
            url = url
        else:
            url = "http://" + url
        pub_date = timezone.datetime.now()
        hunter = request.user
        product = Product(title=title, body=body, icon=icon, image=image, url=url, pub_date=pub_date, hunter=hunter)
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            messages.info(request, 'all fields are required')
            return redirect('create')

    else:

        return render(request, 'products/create.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})

@login_required
def upvote(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=product_id)
        product.votes_total += 1
        product.save()
        return redirect('/products/' + str(product.id))

