from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext

from sales.models import Sale
from sales.forms import SalePaymentForm


def charge(request):
    if request.method == "POST":
        form = SalePaymentForm(request.POST)
        
        if form.is_valid(): # charges the card
            return HttpResponse("Success! We've charged your card!")
    else:
        form = SalePaymentForm()
    
    return render_to_response("sales/charge.html", 
                        RequestContext( request, {'form': form} ) )