import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import Good, Category, Firma
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, status
from .serializers import GoodSerializer, FirmaSerializer, CategorySerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST", "GET"])
def create_category(request):
    if request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(instance=categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PUT", "DELETE"])
def detail_category(request, pk):
    category = generics.get_object_or_404(Category, pk=pk)
    if request.method == "GET":
        serializer = CategorySerializer(instance=category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = CategorySerializer(instance=category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST", "GET"])
def create_firm(request):
    if request.method == 'POST':
        serializer = FirmaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        firms = Firma.objects.all()
        serializer = FirmaSerializer(instance=firms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PUT", "DELETE"])
def detail_firm(request, pk):
    firm = generics.get_object_or_404(Firma, pk=pk)
    if request.method == "GET":
        serializer = FirmaSerializer(instance=firm)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = FirmaSerializer(instance=firm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        firm.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(["POST", "GET"])
def create_good(request):
    if request.method == 'POST':
        serializer = GoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        goods = Good.objects.all()
        serializer = FirmaSerializer(instance=goods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET", "PUT", "DELETE"])
def detail_good(request, pk):
    good = generics.get_object_or_404(Good, pk=pk)
    if request.method == "GET":
        serializer = GoodSerializer(instance=good)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = FirmaSerializer(instance=good, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == "DELETE":
        good.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# @csrf_exempt
# def create_good(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         new_good = Good.objects.create(**data)
#         json_data = {
#             "name": new_good.name,
#             "price": new_good.price,
#             "firm": new_good.firm,
#             "category": new_good.category
#         }
#         return JsonResponse(json_data, safe=False)
#
#     if request.method == "GET":
#         goods = Good.objects.all()
#         data = []
#         for good in goods:
#             data.append(
#                 {
#                     "name": good.name,
#                     "price": good.price,
#                     "firm_id": good.firm.id,
#                     "category_id": good.category.id
#                 }
#             )
#         json_data = json.dumps(data)
#         return JsonResponse(json_data, safe=False)
#
# @csrf_exempt
# def create_firm(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         new_firm = Firma.objects.create(**data)
#         json_data = {
#             "firm_name": new_firm.firm_name,
#             "adress": new_firm.adress
#         }
#         return JsonResponse(json_data, safe=False)
#
#     if request.method == "GET":
#         firms = Firma.objects.all()
#         data = []
#         for firm in firms:
#             data.append(
#                 {
#                     "firm_name": firm.firm_name,
#                     "adress": firm.adress
#                 }
#             )
#         json_data = json.dumps(data)
#         return JsonResponse(json_data, safe=False)

# @csrf_exempt
# def create_category(request):
#     if request.method == "POST":
#         data = json.loads(request.body)
#         new_category = Category.objects.create(**data)
#         json_data = {
#                 "category_name": new_category.category_name
#         }
#         return JsonResponse(json_data, safe=False)
#
#     if request.method == "GET":
#         categories = Category.objects.all()
#         data = []
#         for category in categories:
#             data.append(
#                 {
#                     "category_name": category.category_name
#                 }
#             )
#             json_data = json.dumps(data)
#             return JsonResponse(json_data, safe=False)
#
# class GoodViewSet(viewsets.ModelViewSet):
#     queryset = Good.objects.all()
#     serializer_class = GoodSerializer
#
# class FirmaCreateListView(generics.ListCreateAPIView):
#     queryset = Firma.objects.all()
#     serializer_class = FirmaSerializer
#
# class FirmaRetrieveUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Firma.objects.all()
#     serializer_class = FirmaSerializer







