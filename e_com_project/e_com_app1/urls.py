from django.conf import settings
from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('base', views.base, name='base'),
    path('', views.index, name='index'),
    path('accounts/registration', views.registration_page, name='registration_page'),
    path('profile/<int:id>', views.profile, name='profile'),
    path('add_profile/<int:id>/', views.add_profile, name='add_profile'),
    path('edit_profile/<int:id>/', views.edit_profile, name='edit_profile'),
    path('conatct us', views.conatct, name='conatct'),
    path('about us', views.about, name='about'),
    path('mobiles', views.mobiles, name='mobiles'),
    path('laptop', views.laptop, name='laptop'),
    path('order/<int:id>', views.order, name='order'),
    path('remove_item/<int:id>', views.remove_item, name='remove_item'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('kart', views.kart, name='kart'),
    path('checkout', views.checkout, name='checkout'),
    path('payment_page', views.payment_page, name='payment_page'),
    path('order_page', views.order_page, name='order_page'),
    path('demo', views.demo, name='demo'),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)