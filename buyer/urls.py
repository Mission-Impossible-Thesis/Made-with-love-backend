
from .views import getCategoryItems
from .views import orderItem
from django.urls import path
from django.urls import include, re_path
from .views import payment
# from .views import checkOutItem
# ---> add here the rest of the url 
# path('', signupSeller.as_view(),)


from .views import buyerUsername
from .views import buyerPassword
from .views import buyerLocation
from .views import getAll

urlpatterns = [
    path('userName', buyerUsername.as_view(), ),
    path('location', buyerLocation.as_view(), ),
    path('changePassword', buyerPassword.as_view()),
    path('order', orderItem.as_view(), ),
    path('<slug:cat>', getCategoryItems.as_view(), ),
<<<<<<< HEAD
    path(r'^test-payment/$', payment.as_view(),),
    # path('checkout', checkOutItem.as_view(),)
=======
    path('getAll/' , getAll.as_view(),),
    
>>>>>>> 37bb2d8b27d1ebacabc9168ef5e1b7933c487876

 ]