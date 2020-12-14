from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse("Hello World")
    mydict ={'insert_me':"Hello,now i'm coming from first app/index.html"}
    return render(request,'first_app/index.html',context=mydict)
