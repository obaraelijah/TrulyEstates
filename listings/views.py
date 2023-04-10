from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from django.db.models import Q
from .choices import bedroom_choices,price_choices,state_choices

def index(request):
    listings = Listing.objects.order_by("-list_date")
    paginator = Paginator(listings, 1)
    page= request.GET.get("page")
    paged_listings = paginator.get_page(page)
    context = {
        "listings": paged_listings
    }
    return render(request, "listings/index.html", context)


def listing(request, pk):
    listing = get_object_or_404(Listing, pk )
    context = {
        "listing": listing
    }
    return render(request, "listings/listing.html", context)

def search(request):
    listings = Listing.objects.order_by("-list-date").filter(is_published=True)
    
    #serch by keyword
    keywords = request.GET.get('keywords')
    if keywords:
        listings = listings.filter(description__icontains=keywords)
    
    #search by city or state
    state = request.GET.get('state')
    city = request.GET.get('city')
    if state or city:
        q =Q()
        if state:
            q |= Q(state__iexact=state)
        if city:
            q |= Q(city__iexact=city)
        listings = listings.filter(q)
        
    #search by bedrooms
    bedrooms = request.GET.get('bedrooms')
    if bedrooms:
        listings = listings.filter(bedrooms__lte=bedrooms)
        
    #search by price
    price = request.GET.get('price')
    if price:
        listings = listings.filter(price__lte=price)
        
    context = {
        "state_choices": state_choices,
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "listings": listings,
        'values': {k: v for k, v in request.GET.items() if v}
    }
    return render(request,  "listings/search.html", context)