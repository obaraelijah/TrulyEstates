from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import send_mail
def contacts(request):
    if request.method == 'POST':
       listing_id = request.POST['listing_id']
       listing = request.POST['listing']
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       user_id = request.POST['user_id']
       realtor_email = request.POST['realtor_email']
    
    if request.user.is_authenticated:
        user_id = request.user.id
        has_contacted = Contact.objects.filter(listing_id=listing_id, user_id=user_id)
        if has_contacted:
            messages.error("You have already made an inquiry for the listing")
            return redirect("/listings/"+listing_id)
        
        contact = Contact(
            listing=listing,
            listing_id=listing_id,
            name=name,
            email=email,
            realtor_email=realtor_email,
            message=message,
            user_id=user_id,
            phone=phone
        )
        contact.save()
        send_mail(
            'Property Listing inquiry',
            'There has been an inquiry for '+listing,
            'elijahobara@gmail.com',
            [realtor_email, "obaraee@gmail.com"],
            fail_silently=False,
        )
        
        messages.info(
            request, "Inquiry has been sent,a realtor will get back to you soon")
        return redirect("/listings/"+listing_id
        )
    return render(request, "accounts/dashboard.html")
        
        