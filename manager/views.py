from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader
from .models import Investor

def index(request):
    latest_investor_list = Investor.objects.order_by('-kyc_date')[:5]
    return render(request, 'manager/index.html', {'latest_investor_list': latest_investor_list})

def detail(request, investor_id):
    investor = get_object_or_404(Investor, pk=investor_id)
    return render(request, 'manager/detail.html', {'investor': investor})

def results(request, investor_id):
    response = "You're looking at the results of investor %s."
    return HttpResponse(response % investor_id)

def vote(request, investor_id):
    return HttpResponse("You're voting on investor %s." % investor_id)

# Create your views here.
