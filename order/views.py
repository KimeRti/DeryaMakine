from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from order.models import ShopCartForm, ShopCart


@login_required(login_url='login')
def index(request):
    return render(request, "products/basket.html")


"""@login_required(login_url='/login')
def shop_cart_add(request, proid):
    url = request.META.get('HTTP_REFERER') # get last url

    form = ShopCartForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            current_user = request.user # Access User Session information
            quantity = form.cleaned_data['quantity']

            try:
                q1 = ShopCart.objects.get(user_id=current_user.id, product_id=proid)
            except ShopCart.DoesNotExist:
                q1 = None
            if q1 is not None:
                q1.quantity = q1.quantity + quantity
                q1.save()
            else:
                data = ShopCart(user_id=current_user.id, product_id=proid, quantity=quantity)
                data.save()
                request.session['cart_items'] = ShopCart.objects.filter(user_id=current_user.id).count()
                messages.succes(request, "Product added to cart")
                return HttpResponseRedirect(url)
    return HttpResponseRedirect(reverse('product', args=[proid]))"""
