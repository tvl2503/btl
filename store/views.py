from django.shortcuts import render
from .models import Category, Product
import json
import datetime

# Create your views here.
def store(request):
	allProducts = Product.objects.all()
	allCategories = Category.objects.all()
	category_id = request.GET.get('category', None)
	if category_id is not None:
		allProducts = Product.getProductByID(category_id)
	count = len(allProducts)
	data = {
		'products' : allProducts,
		'categories' : allCategories,
		'count' : count
	}
	return render(request, 'store.html', data)
def cart(request):
	return render(request, 'cart.html')
	