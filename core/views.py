from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from .models import (
    Specialist, MealPlan, Article, Registration, Testimonial,
    Booking, MealPlanPurchase, SpecialistAvailability
)

def home(request):
    # Always redirect to login page
    if not request.user.is_authenticated:
        return redirect('login')
    
    # SIMPLE: Always start with 0 counts for demo
    context = {
        'articles': Article.objects.all()[:6],
        'testimonials': Testimonial.objects.all()[:3],
        'user_bookings_count': 0,    # Will always show 0 initially
        'user_purchases_count': 0,   # Will always show 0 initially
        'total_articles': Article.objects.count(),  # Real count of articles
    }
    return render(request, 'home_authenticated.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('signup')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists!')
            return redirect('signup')
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name
        )
        auth_login(request, user)
        messages.success(request, f'Welcome to HEALS, {user.first_name}!')
        return redirect('home')
    
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.first_name}!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password!')
    
    return render(request, 'login.html')


def logout_view(request):
    auth_logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')


@login_required
def my_purchases(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-created_at')
    purchases = MealPlanPurchase.objects.filter(user=request.user).order_by('-created_at')
    
    context = {
        'bookings': bookings,
        'purchases': purchases,
    }
    return render(request, 'my_purchases.html', context)


@login_required
def specialists(request):
    context = {'specialists': Specialist.objects.all()}
    return render(request, 'specialists.html', context)


@login_required
def specialist_detail(request, pk):
    specialist = get_object_or_404(Specialist, pk=pk)
    
    # Get availability for next 7 days
    today = datetime.now().date()
    available_slots = []
    
    for i in range(7):
        check_date = today + timedelta(days=i)
        day_of_week = check_date.weekday()
        
        availability = SpecialistAvailability.objects.filter(
            specialist=specialist,
            day_of_week=day_of_week,
            is_available=True
        )
        
        for slot in availability:
            existing_booking = Booking.objects.filter(
                specialist=specialist,
                booking_date=check_date,
                booking_time=slot.start_time,
                status__in=['PENDING', 'CONFIRMED']
            ).exists()
            
            if not existing_booking:
                available_slots.append({
                    'date': check_date,
                    'time': slot.start_time,
                    'datetime': datetime.combine(check_date, slot.start_time)
                })
    
    context = {
        'specialist': specialist,
        'available_slots': available_slots[:10],
    }
    return render(request, 'specialist_detail.html', context)


@login_required
def book_consultation(request, pk):
    specialist = get_object_or_404(Specialist, pk=pk)
    
    if request.method == 'POST':
        booking_date = request.POST.get('booking_date')
        booking_time = request.POST.get('booking_time')
        
        booking = Booking.objects.create(
            user=request.user,  # Link to logged-in user
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            specialist=specialist,
            booking_date=booking_date,
            booking_time=booking_time,
            notes=request.POST.get('notes', ''),
            total_amount=specialist.hourly_rate,
            payment_method='M-Pesa',
        )
        
        try:
            send_mail(
                subject=f'Booking Confirmation - HEALS',
                message=f'''
Hello {booking.name},

Your consultation with {specialist.name} has been booked!

📅 Date: {booking.booking_date.strftime("%A, %B %d, %Y")}
⏰ Time: {booking.booking_time.strftime("%I:%M %p")}
💰 Amount: ${booking.total_amount}

Payment Details:
- M-Pesa Paybill: 123456
- Account: BOOKING{booking.id}
- Amount: ${booking.total_amount}

View your bookings: http://localhost:8000/my-purchases/

Thank you for choosing HEALS!
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[booking.email],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, 'Booking confirmed! Check your email for payment details.')
        return redirect('booking_confirmation', booking_id=booking.id)
    
    return redirect('specialist_detail', pk=pk)


def booking_confirmation(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id)
    context = {'booking': booking}
    return render(request, 'booking_confirmation.html', context)


@login_required
def meal_plans(request):
    context = {'meal_plans': MealPlan.objects.all()}
    return render(request, 'meal-plans.html', context)


@login_required
def purchase_meal_plan(request, pk):
    meal_plan = get_object_or_404(MealPlan, pk=pk)
    
    if request.method == 'POST':
        purchase = MealPlanPurchase.objects.create(
            user=request.user,  # Link to logged-in user
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            meal_plan=meal_plan,
            amount_paid=meal_plan.price,
            payment_method='M-Pesa',
        )
        
        try:
            send_mail(
                subject=f'Meal Plan Purchase - HEALS',
                message=f'''
Hello {purchase.name},

Thank you for purchasing "{meal_plan.name}"!

📋 Plan: {meal_plan.name}
🍽️ Type: {meal_plan.diet_type}
📅 Duration: {meal_plan.duration}
💰 Amount: ${purchase.amount_paid}

Payment Details:
- M-Pesa Paybill: 123456
- Account: MEAL{purchase.id}
- Amount: ${purchase.amount_paid}

View your purchases: http://localhost:8000/my-purchases/

Best regards,
HEALS Team
                ''',
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[purchase.email],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, 'Purchase successful! Check your email for payment details.')
        return redirect('purchase_confirmation', purchase_id=purchase.id)
    
    context = {'meal_plan': meal_plan}
    return render(request, 'purchase_meal_plan.html', context)


def purchase_confirmation(request, purchase_id):
    purchase = get_object_or_404(MealPlanPurchase, pk=purchase_id)
    context = {'purchase': purchase}
    return render(request, 'purchase_confirmation.html', context)


def articles(request):
    context = {'articles': Article.objects.all()}
    return render(request, 'articles.html', context)