from django.shortcuts import render
from .models import Item
# Create your views here.

items = [
	{
		"title": "Todo 1",
		"description": "Discription of the todo 1"
	},
	{
		"title": "Todo 2",
		"description": "Discription of the todo 2"
	}
]



def index(request):
	items = Item.objects.all()
	return render(request, "index.html", {"items": items})	
