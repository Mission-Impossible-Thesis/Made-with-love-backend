from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
import json as JSON
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render

from django.core.serializers import json
import jwt
#importinf models of tables
from accounts.models import Item
from accounts.models import Seller
from accounts.models import Buyer
from accounts.models import Category
from accounts.models import Order
class getCategoryStore (APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, cat):
        # data = self.request.data
        print(cat)
        obj = Seller.objects.filter(category = cat)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        data= JSON.loads(json_serialized)
        # print(data)
        return Response (data)
class addItem(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        data = self.request.data
        print(data)
        productName = data['product']
        description = data['description']
        price = data['price']
        category = data['category']
        image = data['url']
        store1 = data['user']
        
        if category == "clothes":
            gender = data['gender']
            size = data['size']
            category_id = Category.objects.get(category_id =200)
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            item = Item.objects.create (productname = productName, store_id=s, description=description, price=price, gender=gender, size=size, image=image, category=200)
            return Response ({'success': 'Add Item'})
        if(category == 'food'):
            types = data['type']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =100)
<<<<<<< HEAD
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price,types=types, image=image, category_id=category_id)
=======
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price,types=types, image=image, category_id=100)
>>>>>>> 37bb2d8b27d1ebacabc9168ef5e1b7933c487876
            return Response ({'success': 'Add Item'})
        if category == 'accessories':
            material = data['material']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =300)
<<<<<<< HEAD
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, image=image, material=material, category=category_id)
=======
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, image=image, material=material, category=300)
>>>>>>> 37bb2d8b27d1ebacabc9168ef5e1b7933c487876
            return Response ({'success': 'Add Item'})
        if category == 'baby products':
            gender = data['gender']
            store = Seller.objects.get(store_id =store1)
            s = store.store_id
            category_id = Category.objects.get(category_id =400)
<<<<<<< HEAD
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, gender=gender, image=image, category=category_id)
=======
            item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, gender=gender, image=image, category=400)
>>>>>>> 37bb2d8b27d1ebacabc9168ef5e1b7933c487876
            return Response ({'success': 'Add Item'})
        # category_id = data['category_id']
        # store_id = data['store_id']
        item = Item.objects.create (productname = productName,store_id=s, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
        item.save()
        return Response ({'success': 'Add Item'})

#to get items for seller
class getItems(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
         print('eeeeeeeeeeeeeeeeeeeeeeeeee')
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         print(json_serialized,"iteeeeeems" )
         return Response(json_serialized)


#to get items for visitor
class getItemsVisit(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
         print('eeeeeeeeeeeeeeeeeeeeeeeeee')
         obj = Item.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         print(json_serialized,"iteeeeeems" )
         return Response(json_serialized)


#to get info for seller profile for visitor
class sellerVisit(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request,pk, format=None):
        print(pk)
        obj1 = Seller.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        # print(json_serialized )
        myData = []
        print(pk,">>>>11111111111111")
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        # print(json_serialized )
        myData.append(json_serialized1)
        myData.append(json_serialized)
        print("mydataaa",myData,"dataaend")
        # dat =   JSON.dumps(myData)
        return Response(json_serialized1)

class deleteItem(APIView):
    permission_classes = (permissions.AllowAny,)  
    def delete(self, request, pk, format=None):
        Item.objects.filter(pk=pk).delete()
        print('Deleeeete')
        return Response('Deleteeeed')

class SnippetDetailSeller(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = (permissions.AllowAny,)
    # def get(self,request,  pk):
    #     try:
    #         return Snippet.objects.get(pk=pk)
    #     except Snippet.DoesNotExist:
    #         raise Http404
    # def get(self, request,pk, format=None):
    #      print('eeeeeeeeeeeeeeeeeeeeeeeeee')
    #      obj = Seller.objects.filter(pk=pk)
    #      json_serializer = json.Serializer()
    #      json_serialized = json_serializer.serialize(obj)
    #      print(json_serialized )
    #      return Response(json_serialized)
    

    # to get info for the seller
    def get(self, request,pk, format=None):
        print(pk)
        #   data = self.request.data 
        # store_Name = data['store_Name'] 
        # description = data['description'] 
        # location = data['location'] 
        # delivery_date = data[' delivery_date '] 
        # image = data['image']
        # category_id = data['category_id']
        # store_id = data['store_id'] 
        # serializer = SnippetSerializer(snippet)
        obj1 = Seller.objects.filter(pk=pk)
        json_serializer = json.Serializer()
        json_serialized1 = json_serializer.serialize(obj1)
        # print(json_serialized )
        myData = []
        print(pk,">>>>11111111111111")
        obj = Item.objects.filter(store_id=pk)
        json_serializer = json.Serializer()
        json_serialized = json_serializer.serialize(obj)
        # print(json_serialized )
        myData.append(json_serialized1)
        myData.append(json_serialized)
        print("mydataaa",myData,"dataaend")
        # dat =   JSON.dumps(myData)
        return Response(json_serialized1)

#to update one item
class updateItem(APIView):
    permission_classes = (permissions.AllowAny,) 
    def post(self, request, pk, format=None):
        obj = Item.objects.get(pk=pk)
        data = self.request.data 
        print(data)

        productName = data['productName'] 
        description = data['description'] 
        price = data['price']
        category = data['category']
        image = data['url'] 

        if category == "clothes":
            gender = data['gender'] 
            size = data['size'] 
            category_id = Category.objects.get(category_id =200)
            Item.objects.save (productname = productName, description=description, price=price, gender=gender, size=size, image=image, category=200)
           
            return Response ({'success': 'Item Editeeed'})
        if(category == 'food'):
            types = data['type'] 
            category_id = Category.objects.get(category_id =100) 
            Item.objects.save (productname = productName, description=description, price=price,types=types, image=image, category_id=100)
            item.save()
            return Response ({'success': 'Item Editeeed'})
        if category == 'accessories':
            material = data['material'] 
            category_id = Category.objects.get(category_id =300)
            Item.objects.save (productname = productName, description=description, price=price, image=image, material=material, category=300)
            item.save()
            return Response ({'success': 'Item Editeeed'})
        if category == 'baby products':
            gender = data['gender']
            category_id = Category.objects.get(category_id =400)
            Item.objects.save (productname = productName, description=description, price=price, gender=gender, image=image, category=400)
            return Response ({'success': 'Item Editeeed'})

        # category_id = data['category_id']
        # store_id = data['store_id'] 
        # item = Item.objects.create (productname = productName, description=description, price=price,  image=image)
        # item.save()
        return Response ({'success': 'Item Editeeeed'})
    # def put(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     serializer = SnippetSerializer(snippet, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def delete(self, request, pk, format=None):
    #     snippet = self.get_object(pk)
    #     snippet.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
        # item = Item.objects.create (productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
        # item.save()
class getListOrder (APIView):
     permission_classes = (permissions.AllowAny,)
     def get(self, request, pk):
         print(pk)
         obj= Order.objects.filter(store_id=pk)
         json_serializer = json.Serializer()
         json_serialized = json_serializer.serialize(obj)
         data= JSON.loads(json_serialized)
         print(data)
         for x in data:
             y=Item.objects.get(item_id = x["fields"]["item"] )
             x["fields"]["item"] =y.productname
             z=Buyer.objects.get(buyer_id = x["fields"]["buyer"] )
             x["fields"]["buyer"]= z.username
         return Response (data)


class  sellerPassword(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         newPassword = data['newPassword']
         password = data['oldPassword']
         user = Seller.objects.get(email= tole)
         print(password,"new" )
         
         s = 'gh@f$#$@&4hjhgjh'
         e = '786huyh8%3h'
         r ="".join(user.password.split(s))
         t = "".join(r.split(e))
         print (t,"db")
         
         if password == t:
             s = 'gh@f$#$@&4hjhgjh'
             e = '786huyh8%3h'
             length = (len(newPassword)/2)
             iy = int(length)
             print(length)
             firstpart = newPassword[0:iy]
             seconedpart = newPassword[iy:len(newPassword)]
             x =newPassword[0] + s + firstpart[1:int(len(firstpart)/2)] + s + firstpart[int(len(firstpart)/2):] + seconedpart[:int(len(seconedpart)/2)] + e + seconedpart[int(len(seconedpart)/2):]
             Seller.objects.filter(email= tole).update(password =x)
             return HttpResponse({"success":"password changed"} ,status="200")
         else:
            return HttpResponse({"Unauthorized":"password incorrect"} ,status="400")

class  sellerStorename(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         storeName= data['storeName']
         Seller.objects.filter(email= tole).update(store_name =storeName )
         return HttpResponse({"success":"location changed"} ,status="200") 
        #  user = Seller.objects.get(email= tole)
        #  if user:
        #      Seller.objects.filter(email= tole).update(store_name =storeName )
        #      return HttpResponse({"success":"location changed"} ,status="200")   
        #  else:
        #     return HttpResponse({"Unauthorized":"password incorrect"} ,status="400")

class editItem (APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, pk):
        data = self.request.data
        if not data:
            return HttpResponse({"Error":"please enter your information"} ,status="401")
        elif data:
            try:
                gender = data['gender']
                size = data['size']
                productName = data['product']
                description = data['description']
                price = data['price']
                image = data['url']
                material = data['material']
                types = data['type']
                image = data['url']
                Item.objects.filter(item_id= pk).update(productname = productName, description=description, price=price, gender=gender,types=types, size=size, image=image, material=material)
                return HttpResponse({"success":"updated"} ,status="200")
            except Item.DoesNotExist:
                return HttpResponse({"Error":"ERROR"} ,status="401")

#to delete one item
class deleteItem(APIView):
    permission_classes = (permissions.AllowAny,)  

class  sellerLocation(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         location= data['location']
         Seller.objects.filter(email= tole).update(location =location )
         return HttpResponse({"success":"location changed"} ,status="200")


class  sellerDelivery(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         delivery= data['delivery']
         Seller.objects.filter(email= tole).update(delivery_time =delivery )
         return HttpResponse({"success":"delivery time changed"} ,status="200")


class  sellerImage(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         image= data['image']
         Seller.objects.filter(email= tole).update(image =image )
         return HttpResponse({"success":"location changed"} ,status="200")

class  sellerDescription(APIView):
     permission_classes = (permissions.AllowAny,)
     def post(self, request,format=None):
         data = self.request.data
         token = request.META.get('HTTP_AUTHORIZATION')
         tole = jwt.decode(token, "SECRET_KEY")['email']
         description= data['description']
         Seller.objects.filter(email= tole).update(description =description )
         return HttpResponse({"success":"description changed"} ,status="200")

class getAll(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION')
        print(token)
        if not token:
             return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        elif token:
                try:
                    tole = jwt.decode(token, "SECRET_KEY")
                    print(tole['email'],'hijuhuyu')
                    email = tole['email']
                    obj11 = Seller.objects.filter(email = email)
                    if obj11:
                        json_serializer = json.Serializer()
                        json_serialized = json_serializer.serialize(obj11)
                        data1= JSON.loads(json_serialized)
                        return Response (data1)
                except jwt.DecodeError:
                    return HttpResponse({"Unauthorized":"Unauthorized"} ,status="401")
        
