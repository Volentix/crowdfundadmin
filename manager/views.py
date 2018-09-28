from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
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
    investor = get_object_or_404(Investor, pk=investor_id)
    investor.public_address = request.POST['public_address']
    investor.save()
    return HttpResponseRedirect(reverse('manager:index'))
