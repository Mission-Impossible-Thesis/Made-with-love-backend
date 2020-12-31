from django.conf.urls import url
from payments import views
from .views import PaymentView
urlpatterns = [
    url('checkout',  PaymentView.as_view(), ),
]