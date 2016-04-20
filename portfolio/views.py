from django.shortcuts import render
from portfolio.models import Item
# Create your views here.
def index(request):
	items = Item.objects.order_by("-date")
	context_dict = {'items': items}
	return render(request, 'portfolio/index.html', context_dict)