from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status
from .serializers import MovieItemSerializers
from .models import bigdata
# Create your views here.

class MovieItemViews(APIView):
    #post func
    def post(self,request):
        serializer = MovieItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                "status":"success",
                "data":serializer.data
            }
            #geri dönüş
            return Response(context,status=status.HTTP_200_OK)

        else:
            context = {
                "status":"success",
                "data":serializer.errors
            }
            return Response(context,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,id=None):
        if id:
            item = bigdata.objects.get(id=id)
            #serializers.py dosyasındaki sınıfa , models.py'daki objelerin id=id olanları at
            serializer = MovieItemSerializers(item)
            context = {
                "status":"success",
                "data":serializer.data
            }
            #geri dönüş
            return Response(context,status=status.HTTP_200_OK)
        #bigdata model objelerini al
        item = bigdata.objects.all()
        serializer = MovieItemSerializers(item,many=True)
        context = {
            "status":"success",
            "data":serializer.data
            }
        return Response (context,status=status.HTTP_200_OK)


    #Güncelle
    def patch(self,request,id=None):
        item = bigdata.objects.get(id=id)
        serializer = MovieItemSerializers(item,data=request.data,partial=True)
        if serializer.is_valid():
            context = {
                "status":"succes",
                "data":serializer.data
            }
            return Response(context,status=status.HTTP_200_OK)

        else:
            return Response({"status":"error","data":serializer.errors})
    #sil
    def delete(self,request,id=None):
        #objeyi getir veya 404 dön ilgili modeldeki id.si eşit olanları
        item = get_object_or_404(bigdata,id=id)
        #sil
        item.delete()
        context = {
                "status":"success",
                "data":"Film Silindi"
            }
        #geri dönüş
        return Response(context)
