from django.contrib import admin
from .models import (
    Specialist, MealPlan, Article, Registration, Testimonial,
    SpecialistAvailability, Booking, MealPlanPurchase
)


# Register your models here.

@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'years_experience', 'hourly_rate', 'rating']

@admin.register(MealPlan)
class MealPlanAdmin(admin.ModelAdmin):
    list_display = ['name', 'diet_type', 'duration', 'calories', 'price']

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'created_at']

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'interest', 'created_at']
    list_filter = ['interest', 'created_at']

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'rating']



# Add admin for new models

@admin.register(SpecialistAvailability)
class SpecialistAvailabilityAdmin(admin.ModelAdmin):
    list_display = ['specialist', 'day_of_week', 'start_time', 'end_time', 'is_available']
    list_filter = ['specialist', 'day_of_week', 'is_available']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'specialist', 'booking_date', 'booking_time', 'status', 'paid', 'total_amount']
    list_filter = ['status', 'paid', 'booking_date']
    search_fields = ['name', 'email', 'phone']
    actions = ['mark_as_confirmed', 'mark_as_paid']
    
    def mark_as_confirmed(self, request, queryset):
        queryset.update(status='CONFIRMED')
    mark_as_confirmed.short_description = "Mark as Confirmed"
    
    def mark_as_paid(self, request, queryset):
        queryset.update(paid=True, status='CONFIRMED')
    mark_as_paid.short_description = "Mark as Paid"

@admin.register(MealPlanPurchase)
class MealPlanPurchaseAdmin(admin.ModelAdmin):
    list_display = ['name', 'meal_plan', 'status', 'paid', 'amount_paid', 'created_at']
    list_filter = ['status', 'paid', 'created_at']
    search_fields = ['name', 'email', 'phone']
    actions = ['mark_as_paid']
    
    def mark_as_paid(self, request, queryset):
        queryset.update(paid=True, status='ACTIVE')
    mark_as_paid.short_description = "Mark as Paid & Activate"