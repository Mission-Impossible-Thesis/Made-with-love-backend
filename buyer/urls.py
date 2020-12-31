
from .views import getCategoryItems
from .views import orderItem
from django.urls import path
from django.urls import include, re_path
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
    path('getAll/' , getAll.as_view(),),
    

 ]