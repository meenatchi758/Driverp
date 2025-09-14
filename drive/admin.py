from django.contrib import admin
from .models import Vision, Mission, Arrow, Biki


admin.site.register(Vision)
admin.site.register(Mission)

admin.site.register(Arrow)

@admin.register(Biki)
class BikiAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'engine_cc', 'price', 'kilometers', 'fuel_type', 'ownership', 'location')
    search_fields = ('name', 'location')
    list_filter = ('year', 'fuel_type', 'ownership')

from .models import Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')


from .models import HeroSection

@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ('heading',)
    search_fields = ('heading', 'subtext')


from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "short_answer")
    search_fields = ("question", "answer")

    def short_answer(self, obj):
        return obj.answer[:60] + "..." if len(obj.answer) > 60 else obj.answer
    short_answer.short_description = "Answer"

# admin.py
from .models import About

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ("title", "image")


from .models import Chango

admin.site.register(Chango)

from django.contrib import admin
from .models import Approach

admin.site.register(Approach)


from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'reason', 'found_us', 'timestamp')
    list_filter = ('reason', 'found_us', 'timestamp')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'reason', 'found_us', 'message', 'timestamp')


from .models import BikeAd

@admin.register(BikeAd)
class BikeAdAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']

from .models import ProcessStep


@admin.register(ProcessStep)
class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    ordering = ('id',)
    search_fields = ('title',)


from .models import  BookingStep



@admin.register(BookingStep)
class BookingStepAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'description')
    ordering = ('order',)

from django.contrib import admin
from django.utils.html import format_html
from .models import LoginImage

@admin.register(LoginImage)
class LoginImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height:auto;" />', obj.image.url)
        return "(No image)"

    image_preview.short_description = 'Preview'


