from django.shortcuts import render
from .models import *
from django.http import JsonResponse
# Create your views here.
def home(request):
    return render(request,'home.html')

def api_hotel(request):
    hotels_objs = Hotels.objects.all()

    price = request.GET.get('price')
    #To get price less than the given price then we use price__lte = price and if we need more we will use price__gte.
    if price:
        hotels_objs = hotels_objs.filter(price__lte = price)
    emenities = request.GET.get('emenities')
    if emenities:
        emenities = emenities.split(',')
        em = []
        for e in emenities:
            try :
                es.append(int(e))
            except Exception as e:
                pass
        hotels_objs = hotels_objs.filter(emenities__in = em).distinct 
        




    payload=[]
    for hotel_obj in hotels_objs:
        result = {}
        result['hotel_name'] = hotel_obj.hotel_name
        result['hotel_description'] = hotel_obj.hotel_description
        result['hotel_image'] = hotel_obj.hotel_image
        result['hotel_price'] = hotel_obj.price
        payload.append(result)
    return JsonResponse(payload , safe = False)



