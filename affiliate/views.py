from django.shortcuts import render
from .models import Deal


def home(request):
    deals = Deal.objects.order_by('-created')[:6]
    context = {
        'deals': deals,
    }
    return render(request, 'index.html', context)
