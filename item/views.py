from django.shortcuts import render
from .models import Item
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

# items = [
# 	{
# 		"title": "Todo 1",
# 		"description": "Discription of the todo 1"
# 	},
# 	{
# 		"title": "Todo 2",
# 		"description": "Discription of the todo 2"
# 	}
# ]



def index(request):
	items = Item.objects.all()
	return render(request, "index.html", {"items": items})	

def add(request):
	return render(request, "add.html")	

def addrecord(request):
	# _title=request.POST['title']
	_description=request.POST['description']
	items=Item(description=_description)
	items.save()
	return HttpResponseRedirect(reverse('index'))


