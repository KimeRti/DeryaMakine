import json
import urllib.parse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from order.models import ShopCartForm, ShopCart, OrderForm, Order, OrderDetail
from django.views.decorators.http import require_http_methods
import hashlib
import base64
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

SANAL_POS = {
    'customer_id': '400235',
    'merchant_id': '496',
    'username': 'apitest',
    'password': 'api123',
    'ok_url': 'http://127.0.0.1:8000/order/ok-url/',
    'fail_url': 'http://127.0.0.1:8000/order/fail-url/',
    'card_accept_url': 'https://boatest.kuveytturk.com.tr/boa.virtualpos.services/Home/ThreeDModelPayGate',
    'payment_accept_url': 'https://boatest.kuveytturk.com.tr/boa.virtualpos.services/Home/ThreeDModelProvisionGate',
}


@require_http_methods(["POST"])
def payment(request):
    shopcart = ShopCart.objects.filter(user_id=request.user.id)
    total = 0
    title = ''
    for rs in shopcart:
        total += rs.quantity * rs.product.price
        title += f"{rs.product.title} ({rs.quantity} adet), "
    order = Order()
    order.user_id = request.user.id
    order.total = total
    order.title = title
    order.name = request.POST.get('name')
    order.surname = request.POST.get('surname')
    order.address = request.POST.get('address')
    order.city = request.POST.get('city')
    order.country = request.POST.get('country')
    order.phone = request.POST.get('phone')
    order.email = request.POST.get('email')
    order.note = request.POST.get('note')
    order.status = 'New'
    order.save()
    for rs in shopcart:
        detail = OrderDetail()
        detail.order = order
        detail.product = rs.product
        detail.user_id = request.user.id
        detail.quantity = rs.quantity
        detail.price = rs.product.price
        detail.total = rs.amount
        detail.save()
    for rs in shopcart:
        rs.delete()
    name = request.POST.get('cardname')
    number = request.POST.get('number').replace(' ', '')
    year = request.POST.get('year')
    month = request.POST.get('month')
    cvv = request.POST.get('cvv')
    amount = 5*100
    merchant_order_id = 'web-odeme'
    hashed_password = base64.b64encode(hashlib.sha1(f"{SANAL_POS['password']}".encode('ISO-8859-9')).digest()).decode()
    hashed_data = base64.b64encode(hashlib.sha1(f"{SANAL_POS['merchant_id']}{merchant_order_id}{amount}{SANAL_POS['ok_url']}{SANAL_POS['fail_url']}{SANAL_POS['username']}{hashed_password}".encode('ISO-8859-9')).digest()).decode()
    data = f"""
    <KuveytTurkVPosMessage xmlns:xs="http://www.w3.org/2001/XMLSchema-instance"
        xsd="http://www.w3.org/2001/XMLSchema">
        <APIVersion>1.0.0</APIVersion>
        <OkUrl>{str(SANAL_POS['ok_url'])}</OkUrl>
        <FailUrl>{str(SANAL_POS['fail_url'])}</FailUrl>
        <HashData>{hashed_data}</HashData>
        <MerchantId>{int(SANAL_POS['merchant_id'])}</MerchantId>
        <CustomerId>{str(SANAL_POS['customer_id'])}</CustomerId>
        <UserName>{str(SANAL_POS['username'])}</UserName>
        <CardNumber>{str(number)}</CardNumber>
        <CardExpireDateYear>{str(year)}</CardExpireDateYear>
        <CardExpireDateMonth>{str(month)}</CardExpireDateMonth>
        <CardCVV2>{str(cvv)}</CardCVV2>
        <CardHolderName>{str(name)}</CardHolderName>
        <CardType>Master</CardType>
        <TransactionType>Sale</TransactionType>
        <InstallmentCount>{int('0')}</InstallmentCount>
        <Amount>{int(amount)}</Amount>
        <DisplayAmount>{int(amount)}</DisplayAmount>
        <CurrencyCode>{str('0949')}</CurrencyCode>
        <MerchantOrderId>{str(merchant_order_id)}</MerchantOrderId>
        <TransactionSecurity>{int('3')}</TransactionSecurity>
    </KuveytTurkVPosMessage>
    """

    headers = {'Content-Type': 'application/xml'}
    r = requests.post(SANAL_POS['card_accept_url'], data=data.encode('ISO-8859-9'), headers=headers)
    return HttpResponse(r)


@require_http_methods(["POST"])
@csrf_exempt
def ok_url(request):
    gelen = request.POST.get('AuthenticationResponse')
    data = urllib.parse.unquote(gelen)
    merchant_order_id_start = data.find('<MerchantOrderId>')
    merchant_order_id_stop = data.find('</MerchantOrderId>')
    merchant_order_id = data[merchant_order_id_start + 17:merchant_order_id_stop]
    amount_start = data.find('<Amount>')
    amount_end = data.find('</Amount>')
    amount = data[amount_start + 8:amount_end]
    md_start = data.find('<MD>')
    md_end = data.find('</MD>')
    md = data[md_start + 4:md_end]
    hashed_password = base64.b64encode(
        hashlib.sha1(SANAL_POS["password"].encode('ISO-8859-9')).digest()).decode()
    hashed_data = base64.b64encode(hashlib.sha1(
        f'{SANAL_POS["merchant_id"]}{merchant_order_id}{amount}{SANAL_POS["username"]}{hashed_password}'.encode(
            "ISO-8859-9")).digest()).decode()
    xml = f"""
        <KuveytTurkVPosMessage xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xmlns:xsd="http://www.w3.org/2001/XMLSchema">
        <APIVersion>1.0.0</APIVersion>
        <HashData>{hashed_data}</HashData>
        <MerchantId>{int(SANAL_POS['merchant_id'])}</MerchantId>
        <CustomerId>{int(SANAL_POS['customer_id'])}</CustomerId>
        <UserName>{str(SANAL_POS['username'])}</UserName>
        <TransactionType>Sale</TransactionType>
        <InstallmentCount>0</InstallmentCount>
        <Amount>{amount}</Amount>
        <MerchantOrderId>{str(merchant_order_id)}</MerchantOrderId>
        <TransactionSecurity>3</TransactionSecurity>
        <KuveytTurkVPosAdditionalData>
        <AdditionalData>
        <Key>MD</Key>
        <Data>{md}</Data>
        </AdditionalData>
         </KuveytTurkVPosAdditionalData>
        </KuveytTurkVPosMessage>
        """
    headers = {'Content-Type': 'application/xml'}
    r = requests.post(SANAL_POS['payment_accept_url'], data=xml.encode('ISO-8859-9'), headers=headers)
    return HttpResponse(r, paymentsucces(request))


@require_http_methods(["POST"])
@csrf_exempt
def fail_url(request):
    order = Order.objects.filter(user_id=request.user.id).last()
    order.delete()
    messages.error(request, "Ödeme işlemi başarısız.")
    return render(request, 'order/checkout.html')


@login_required(login_url='login')
def index(request):
    data = ShopCart.objects.filter(user_id=request.user.id)
    return render(request, "order/basket.html", {'shopcarts': data})


@login_required(login_url='/login')
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
                messages.success(request, "Ürün Başarıyla Sepete Eklendi")
                return HttpResponseRedirect(url)
    return HttpResponseRedirect(reverse('productdetail', args=[proid]))


@login_required(login_url='/login')
def shop_cart_delete(request, id):
    url = request.META.get('HTTP_REFERER')
    ShopCart.objects.filter(id=id).delete()
    request.session['cart_items'] = ShopCart.objects.filter(user_id=request.user.id).count()
    messages.success(request, "Ürün Başarıyla Silindi")
    return HttpResponseRedirect(url)


@login_required(login_url='/login')
def checkout(request):
    form = OrderForm(request.POST or None)
    shopcart = ShopCart.objects.filter(user_id=request.user.id)
    context = {
        'form': form,
        'shopcarts': shopcart
    }
    request.session['id'] = request.user.id
    return render(request, 'order/checkout.html', context)


def paymentsucces(request):
    order = Order.objects.get(user=request.user.id)
    order.status = 'Accepted'
    order.save()
    return render(request, 'order/payment-succes.html')
