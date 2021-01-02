# from django import path 
from .views import signupSeller
from .views import Login
from .views import signupBuyer
from .views import Login
from django.urls import path

urlpatterns = [
    path('seller/signup', signupSeller.as_view(),),
    path('buyer/signup', signupBuyer.as_view(),),
    path('login', Login.as_view(),),
    path('buyer/signup', signupBuyer.as_view(),)
    
    ,
    # path('login', Login.as_view(),)

]
