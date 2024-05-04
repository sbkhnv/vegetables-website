from django.urls import path
from .views import LandingPageView,ShopPageView,productdetailView


app_name = 'shop'

urlpatterns = [
    path('shop.html',ShopPageView.as_view(),name="shop"),
    path('',LandingPageView.as_view(),name='landing-page'),
]