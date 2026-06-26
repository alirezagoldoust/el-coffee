from django.shortcuts import render
from .models import Category, MenuItem


def menu(request):
    categories = Category.objects.prefetch_related('items').all()
    specials = MenuItem.objects.filter(is_special=True, is_available=True).select_related('category')
    return render(request, 'menu/index.html', {
        'categories': categories,
        'specials': specials,
    })
