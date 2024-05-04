from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.views import View


class LandingPageView(View):
    def get(self,request):
        return render(request,"landing_page.html")


class ShopPageView(View):
    def get(self,request):
        return render(request,"shop.html")


def productdetailView(request, id):
    product_d = productModel.objects.get(id=id)
    product_m = productModel.objects.order_by('?')[:4]
    return render(request, template_name='shop-detail.html', context={"product_d":product_d, "product_m":product_m})

