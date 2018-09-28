from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Investor

class IndexView(generic.ListView):
    template_name = 'manager/index.html'
    context_object_name = 'latest_investor_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Investor.objects.order_by('-kyc_date')[:5]

class DetailView(generic.DetailView):
    model = Investor
    template_name = 'manager/detail.html'

def vote(request, investor_id):
    investor = get_object_or_404(Investor, pk=investor_id)
    investor.public_address = request.POST['public_address']
    investor.save()
    return HttpResponseRedirect(reverse('manager:index'))
