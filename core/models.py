from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model  # ADD THIS

# Get the User model
User = get_user_model()  # ADD THIS

# Create your models here.

class Specialist(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    years_experience = models.IntegerField()
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(upload_to='specialists/', null=True, blank=True)
    rating = models.FloatField(default=5.0)
    
    def __str__(self):
        return self.name


class MealPlan(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    diet_type = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='meal-plans/', null=True, blank=True)
    
    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class Registration(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    interest = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField(default=5)
    photo = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    
    def __str__(self):
        return self.name
    


# ADD new models:

class SpecialistAvailability(models.Model):
    DAYS_OF_WEEK = [
        (0, 'Monday'),
        (1, 'Tuesday'),
        (2, 'Wednesday'),
        (3, 'Thursday'),
        (4, 'Friday'),
        (5, 'Saturday'),
        (6, 'Sunday'),
    ]
    
    specialist = models.ForeignKey('Specialist', on_delete=models.CASCADE, related_name='availability')
    day_of_week = models.IntegerField(choices=DAYS_OF_WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_available = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['day_of_week', 'start_time']
    
    def __str__(self):
        return f"{self.specialist.name} - {self.get_day_of_week_display()} {self.start_time}-{self.end_time}"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Payment'),
        ('CONFIRMED', 'Confirmed'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    # ADD THIS LINE - Link to Django User
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_bookings', null=True, blank=True)
    
    # User info
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Booking details
    specialist = models.ForeignKey('Specialist', on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateField()
    booking_time = models.TimeField()
    duration = models.IntegerField(default=60, help_text="Duration in minutes")
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True)
    
    # Payment
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, blank=True)
    payment_reference = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['specialist', 'booking_date', 'booking_time']
    
    def __str__(self):
        return f"{self.name} - {self.specialist.name} on {self.booking_date}"
    
    def get_booking_datetime(self):
        from datetime import datetime, time
        return datetime.combine(self.booking_date, self.booking_time)


class MealPlanPurchase(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending Payment'),
        ('ACTIVE', 'Active'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    
    # ADD THIS LINE
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_purchases', null=True, blank=True)

    # User info
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Plan details
    meal_plan = models.ForeignKey('MealPlan', on_delete=models.CASCADE, related_name='purchases')
    start_date = models.DateField(default=timezone.now)
    
    # Status
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    
    # Payment
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, blank=True)
    payment_reference = models.CharField(max_length=100, blank=True)
    paid = models.BooleanField(default=False)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.meal_plan.name}"