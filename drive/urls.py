from django.urls import path
from . import views

from django.http import HttpResponse


urlpatterns = [
    path('', views.home_view, name='home'),                         # Home page
    path('about/', views.about, name='about'),                      # About page
    path('contact/', views.contact_view, name='contact'),           # Contact form
    path('success/', lambda request: HttpResponse(                  # Contact success
        "✅ Thank you for contacting us. Our team will reach out to you soon."
    ), name='contact_success'),

    path('bikes/', views.combined_view, name='sellbike'),           # Sell bike
    path('buybikes/', views.bike_list_html, name='buybikes'),       # Buy bike list
    path('bike/<int:pk>/', views.bike_detail, name='bike_detail'),  # Bike detail
    path('book/<int:pk>/', views.book_bike, name='book_bike'), 
     path('login/', views.login_view, name='login'),
            path('payment/<int:bike_id>/', views.payment_view, name='payment'), 


]


