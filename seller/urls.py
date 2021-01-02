from django.urls import path
from django.urls import include, re_path
from .views import getCategoryStore
from .views import addItem
from .views import SnippetDetailSeller
from .views import getItems
from .views import getItemsVisit
from .views import sellerVisit
from .views import deleteItem
from .views import updateItem

from .views import getListOrder
from .views import deleteItem
from .views import sellerPassword
from .views import sellerStorename
from .views import sellerLocation
from .views import sellerDelivery
from .views import sellerImage
from .views import sellerDescription
from .views import editItem
from .views import getAll
# from .views import sellerStoreId
urlpatterns = [
 path('changePassword', sellerPassword.as_view()),
 path('editProfile/<int:pk>', editItem.as_view(), ),
 path('storeName', sellerStorename.as_view()),
 path('location', sellerLocation.as_view()),
 path('description', sellerDescription.as_view()),
 path('delivery', sellerDelivery.as_view()),
 path('image', sellerImage.as_view()),
 path('addItem', addItem .as_view(), ),    
 path('<slug:cat>', getCategoryStore.as_view(), ),  
 path('profile/deleteitems/<int:pk>', deleteItem .as_view(), ),
 path('editProfile', SnippetDetailSeller.as_view()),
 path('profile/<int:pk>', SnippetDetailSeller.as_view()),
 path('profile/items/<int:pk>', getItems.as_view()),
 path('visit/items/<int:pk>', getItemsVisit.as_view()),
 path('visit/<int:pk>', sellerVisit.as_view()),
 path('getAll/' , getAll.as_view(),),
#  path('changestoreid', sellerStoreId.as_view()),
 path('order/list/<int:pk>', getListOrder.as_view(), ),

 ]
