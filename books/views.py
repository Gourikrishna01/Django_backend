from django.shortcuts import render
from django.http import HttpResponse
from.models import BookModel
from django.db.models import Q
import json
from books.serializer import BookSerializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def Add(request):
    if request.method=='POST':
        recived_data=json.loads(request.body)
        print(recived_data)
        serialized_check=BookSerializer(data=recived_data)
        if serialized_check.is_valid():
            serialized_check.save()
            return HttpResponse(json.dumps({'status':"sucsses"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))

@csrf_exempt
def viewAll(request):
    if request.method=='POST':
        book_list=BookModel.objects.all()
        serialized_data=BookSerializer(book_list,many=True)
        return HttpResponse(json.dumps(serialized_data.data))
@csrf_exempt
def Search(request):
    if request.method=='POST':
        recived_data=json.loads(request.body)
        get_data=recived_data["title"]
        data=list(BookModel.objects.filter(Q(title__icontains=get_data)).values())
        return HttpResponse(json.dumps(data))

@csrf_exempt
def Delete(request):
    if request.method=='GET':
        return HttpResponse(json.dumps({"status":"deleted"}))

