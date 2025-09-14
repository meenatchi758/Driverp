import base64
from django.shortcuts import render
from .models import Biki, Vision, Mission, Arrow, Testimonial, HeroSection, FAQ

def home_view(request):
    bikes = Biki.objects.all()

    # Convert binary image data to base64
    for bike in bikes:
        if hasattr(bike, 'image_data') and bike.image_data:
            bike.image_base64 = base64.b64encode(bike.image_data).decode('utf-8')
        else:
            bike.image_base64 = None

    vision = Vision.objects.first()
    mission = Mission.objects.first()
    arrows = Arrow.objects.all()
    testimonials = Testimonial.objects.all()
    hero = HeroSection.objects.first()
    faqs = FAQ.objects.all()

    context = {
        'bikes': bikes,
        'vision': vision,
        'mission': mission,
        'arrows': arrows,
        'testimonials': testimonials,
        'hero': hero,
        'faqs': faqs
        
        
    }
    return render(request, 'drive/home.html', context)
# ------------------------------------------------------------------------ABOUT------------------------------------------
from .models import About, Chango, Approach
from django.shortcuts import render

def about(request):
    about_data = About.objects.first()
    chango_data = Chango.objects.first()
    approach = Approach.objects.first()  # ✅ FIXED

    return render(request, "drive/about.html", {
        "about": about_data,
        "chango": chango_data,
        "approach": approach
    })
# --------------------------------------------------------------------CONTACT---------------------------------------------------------------
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

from .forms import ContactMessageForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            user_email = form.cleaned_data['email']
            user_message = form.cleaned_data['message']

            # Email to admin
            admin_subject = f"New contact message from {name}"
            admin_message = f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{user_message}"
            admin_email = 'admin@example.com'  # replace with actual admin email

            send_mail(
                admin_subject,
                admin_message,
                settings.DEFAULT_FROM_EMAIL,
                [admin_email],
            )

            # Confirmation email to user
            user_subject = "Thank you for contacting us"
            user_message_body = (
                f"Hi {name},\n\n"
                "Thank you for reaching out! We received your message and will get back to you soon.\n\n"
                f"Your message:\n{user_message}\n\n"
                "Best regards,\nAdmin Team"
            )

            send_mail(
                user_subject,
                user_message_body,
                settings.DEFAULT_FROM_EMAIL,
                [user_email],
            )

            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Adjust 'contact' to your url name

        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = ContactMessageForm()

    return render(request, 'drive/contact.html', {'form': form})
# ------------------------------------------------------------------------------SELL BIKE--------------------------------------
from django.shortcuts import render
from .models import BikeAd, ProcessStep

def combined_view(request):
    bikes = BikeAd.objects.all()
    steps = ProcessStep.objects.all().order_by('id')  


    return render(request, 'drive/sellbike.html', {
        'bikes': bikes,
        'steps': steps,
    })
# -----------------------------------------------------------------------BUY BIKE-------------------------------------
from django.shortcuts import render
from .models import Bikes

def bike_list_html(request):
    bikes = Bikes.objects.all()

    # --- Filters ---
    budget_min = request.GET.get('budget_min')
    budget_max = request.GET.get('budget_max')
    brand = request.GET.getlist('brand')
    category = request.GET.getlist('category')
    year_min = request.GET.get('year_min')
    year_max = request.GET.get('year_max')
    kilometers_min = request.GET.get('km_min')
    kilometers_max = request.GET.get('km_max')
    engine_min = request.GET.get('engine_min')
    engine_max = request.GET.get('engine_max')
    fuel_type = request.GET.getlist('fuel_type')
    color = request.GET.getlist('color')

    # Apply filters
    if budget_min:
        bikes = bikes.filter(price__gte=int(budget_min))
    if budget_max:
        bikes = bikes.filter(price__lte=int(budget_max))
    if brand:
        bikes = bikes.filter(brand__in=brand)
    if category:
        bikes = bikes.filter(category__in=category)
    if year_min:
        bikes = bikes.filter(year__gte=int(year_min))
    if year_max:
        bikes = bikes.filter(year__lte=int(year_max))
    if kilometers_min:
        bikes = bikes.filter(kilometers__gte=int(kilometers_min))
    if kilometers_max:
        bikes = bikes.filter(kilometers__lte=int(kilometers_max))
    if engine_min:
        bikes = bikes.filter(engine_cc__gte=int(engine_min))
    if engine_max:
        bikes = bikes.filter(engine_cc__lte=int(engine_max))
    if fuel_type:
        bikes = bikes.filter(fuel_type__in=fuel_type)
    if color:
        bikes = bikes.filter(color__in=color)

    # --- Sorting ---
    sort_by = request.GET.get('sort', 'newest')
    if sort_by == 'price_asc':
        bikes = bikes.order_by('price')
    elif sort_by == 'price_desc':
        bikes = bikes.order_by('-price')
    elif sort_by == 'km_asc':
        bikes = bikes.order_by('kilometers')
    elif sort_by == 'km_desc':
        bikes = bikes.order_by('-kilometers')
    elif sort_by == 'year_asc':
        bikes = bikes.order_by('year')
    elif sort_by == 'year_desc':
        bikes = bikes.order_by('-year')
    else:
        bikes = bikes.order_by('-id')

    # Get filter options
    all_brands = Bikes.objects.values_list('brand', flat=True).distinct()
    all_categories = Bikes.objects.values_list('category', flat=True).distinct()
    all_fuel_types = Bikes.objects.values_list('fuel_type', flat=True).distinct()
    all_colors = Bikes.objects.values_list('color', flat=True).distinct()

    # Parse selected values for template use
    context = {
        'bikes': bikes,
        'selected_sort': sort_by,
        'all_brands': all_brands,
        'all_categories': all_categories,
        'all_fuel_types': all_fuel_types,
        'all_colors': all_colors,

        # raw GET data for input values
        'filters': request.GET,

        # parsed checkboxes for template logic
        'selected_categories': category,
        'selected_brands': brand,
        'selected_fuels': fuel_type,
        'selected_colors': color,
    }

    return render(request, 'drive/bikelist.html', context)

from django.shortcuts import render, get_object_or_404
from .models import BikesDetail, BookingStep

# 🏍️ List all bikes
def bike_list(request):
    bikes = BikesDetail.objects.all()
    return render(request, 'drive/bikelist.html', {'bikes': bikes})


# 📄 Bike detail + 3 easy steps
def bike_detail(request, pk):
    bike = get_object_or_404(BikesDetail, pk=pk)
    steps = BookingStep.objects.order_by('order')
    return render(request, 'drive/bikedetail.html', {
        'bike': bike,
        'steps': steps
    })


# ✅ Book a bike + show confirmation + steps
def book_bike(request, pk):
    bike = get_object_or_404(BikesDetail, pk=pk)
    bike.is_booked = True
    bike.save()
    steps = BookingStep.objects.order_by('order')
    return render(request, 'drive/bikedetail.html', {
        'bike': bike,
        'steps': steps,
        'message': 'Bike booked successfully!'
    })

# --------------------------------------------------------------------LOGIN--------------------------------------------------


# views.py
from django.shortcuts import render
from .models import LoginImage

def login_view(request):
    login_image = LoginImage.objects.first()  # Get the first image from DB
    return render(request, 'drive/login.html', {'login_image': login_image})


from .models import BikesDetail  # instead of Bike

def payment_view(request, bike_id):
    bike = get_object_or_404(BikesDetail, pk=bike_id)
    price = request.GET.get('price')

    try:
        subtotal = float(price)
    except (TypeError, ValueError):
        subtotal = bike.price  # fallback

    gst = 1000
    test_drive_fee = 1000
    total = subtotal + gst + test_drive_fee

    context = {
        'bike': bike,
        'subtotal': subtotal,
        'gst': gst,
        'test_drive_fee': test_drive_fee,
        'total': total,
    }

    return render(request, 'drive/payment.html', context)








