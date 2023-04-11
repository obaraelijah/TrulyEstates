from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("pages.urls")),
    path("account/", include("account.urls")),
    path("listings/", include("listings.urls")),
    path("contacts/", include("contacts.urls")),
    path('admin/', admin.site.urls),    
]
