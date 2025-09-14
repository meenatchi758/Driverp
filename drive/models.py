
# ----------------------------------------------------------------HOME---------------------------------------------------------------

from django.db import models

class Vision(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image1 = models.ImageField(upload_to='vision_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='vision_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='vision_images/', blank=True, null=True)
    image4 = models.ImageField(upload_to='vision_images/', blank=True, null=True)
    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='mission_images/')

    def __str__(self):
        return self.title



class Bike(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bikes/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Arrow(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='arrows/')  # Main image
    bg_image = models.ImageField(upload_to='arrow_backgrounds/', blank=True, null=True)  # Background image

    def __str__(self):
        return self.title
    
from django.db import models

class Biki(models.Model):
    # Basic bike details
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    engine_cc = models.PositiveIntegerField()
    engine_type = models.CharField(max_length=50, default="FTS")  # e.g., FTS, BS6, DTSi
    kilometers = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50)
    ownership = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)

    # Images (optional)
    image_base64 = models.TextField(blank=True, null=True)
    image_type = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(upload_to='bike_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)

    # Custom display for engine info
    def formatted_engine_info(self):
        return f"{self.engine_cc}CC {self.engine_type.upper()}"

    # Optional: Display full info string (can be used in admin or templates)
    def display_info(self):
        return f"{self.name} ({self.year}) - {self.formatted_engine_info()} - ₹{self.price} - {self.location}"

    # String representation for admin or console
    @property
    def formatted_price(self):
        x = int(self.price)
        s = str(x)[::-1]
        groups = []
        groups.append(s[:3])
        s = s[3:]
        while s:
            groups.append(s[:2])
            s = s[2:]
        return ','.join(groups)[::-1]

    def __str__(self):
        return self.display_info()



from django.db import models

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)  # e.g., "First-Time Buyer"
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')  # Store image uploads here

    def __str__(self):
        return f"{self.name} – {self.role}"
    
class HeroSection(models.Model):
    heading = models.CharField(max_length=200)
    subtext = models.TextField()
    image = models.ImageField(upload_to='hero_images/')



class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question
# ---------------------------------------------------------------ABOUT-----------------------------------------------------

class About(models.Model):
    title = models.CharField(max_length=200, default="About Us")
    description = models.TextField()
    image = models.ImageField(upload_to="about/")

    def __str__(self):
        return self.title



class Chango(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    background_image = models.ImageField(upload_to='chango_backgrounds/')

    def __str__(self):
        return self.title
    

class Approach(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='approach_images/')

# --------------------------------------------------------------CONTACT-----------------------------------------------------


class ContactMessage(models.Model):
    REASONS = [
        ('general', 'General Enquiry'),
        ('buy', 'Buy a Bike'),
        ('sell', 'Sell a Bike'),
        ('exchange', 'Exchange a Bike'),
        ('rto', 'RTO Service'),
        ('others', 'Others'),
    ]

    FOUND_US_CHOICES = [
        ('olx', 'OLX'),
        ('instagram', 'Instagram'),
        ('youtube', 'Youtube'),
        ('google', 'Google'),
        ('website', 'Website'),
        ('facebook', 'Facebook'),
        ('walkin', 'Walk-in'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    reason = models.CharField(max_length=20, choices=REASONS)
    found_us = models.CharField(max_length=20, choices=FOUND_US_CHOICES)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.reason}"

# -----------------------------------------------------------------------SELL BIKE--------------------------------------------

class BikeAd(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bike_images/')
    description = models.TextField()

    def __str__(self):
        return self.title


class ProcessStep(models.Model):
    title = models.CharField(max_length=100)

    image = models.ImageField(upload_to='process_steps/')  # images stored in media/process_steps/

    def __str__(self):
        return self.title
# --------------------------------------------------------------------BUY BIKE--------------------------------------------------


class Bikes(models.Model):
    # Basic info
    year = models.PositiveIntegerField()
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    engine_cc = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    
    # Details
    kilometers = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    owner_info = models.CharField(max_length=100, blank=True)
    image_url = models.URLField(blank=True)
    is_booked = models.BooleanField(default=False)
    image = models.ImageField(upload_to='bike1_images/', blank=True, null=True)

    

    def __str__(self):
        return f"{self.year} | {self.brand} {self.model} | {self.engine_cc}CC"

 
from django.db import models

class BikesDetail(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    variant = models.CharField(max_length=100, blank=True)
    year = models.IntegerField()
    refurbished = models.BooleanField(default=False)
    rto_state = models.CharField(max_length=100, blank=True)
    rto_city = models.CharField(max_length=100, blank=True)
    registration_year = models.IntegerField(null=True, blank=True)
    kilometers = models.PositiveIntegerField()
    owners = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    fuel_type = models.CharField(max_length=50)
    registration_certificate = models.BooleanField(default=False)
    finance = models.BooleanField(default=False)
    price = models.PositiveIntegerField()
    insurance = models.BooleanField(default=False)
    warranty = models.BooleanField(default=False)
    bike_type = models.CharField(max_length=100)
    color = models.CharField(max_length=50)
    ignition_type = models.CharField(max_length=50, blank=True)
    transmission_type = models.CharField(max_length=50)
    front_brake_type = models.CharField(max_length=50)
    rear_brake_type = models.CharField(max_length=50)
    abs = models.BooleanField(default=False)
    odometer = models.CharField(max_length=50)
    wheel_type = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='bike_images/')
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"



class BookingStep(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='booking_steps/')
    order = models.IntegerField()

    def __str__(self):
        return self.title
    

from django.db import models

class LoginImage(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='login_images/')

    def __str__(self):
        return self.title or "Login Image"


