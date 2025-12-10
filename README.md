# 🏥 HEALS - Healthy Eat Long Span

<div align="center">

![HEALS Logo](https://cdn-icons-png.flaticon.com/512/2382/2382533.png)

**Your Complete Health & Wellness Platform**

[![Django](https://img.shields.io/badge/Django-5.2-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Tech Stack](#-tech-stack)

</div>

---

## 📖 About The Project

**HEALS** (Healthy Eat Long Span) is a comprehensive web-based platform designed to revolutionize how people approach nutrition and wellness. Whether you're managing a chronic condition like diabetes, pursuing weight loss goals, or simply seeking a healthier lifestyle, HEALS provides personalized nutrition guidance through expert consultations, customized meal plans, and educational resources.

### 🎯 Mission

To make expert nutritional guidance accessible and affordable for everyone, regardless of their health status or financial situation.

### 💡 Problem Statement

- Limited access to qualified nutritionists and dietitians
- Expensive one-on-one consultations
- Generic diet plans that don't account for individual needs
- Contradictory health advice online
- Growing rates of diabetes and obesity requiring specialized dietary guidance

### ✨ Our Solution

A one-stop platform that combines:
- 👨‍⚕️ Expert specialist consultations
- 🍽️ Personalized meal planning
- 📚 Educational health articles
- 📊 Progress tracking dashboard
- 💳 Affordable pricing with flexible payment options

---

## 🚀 Features

### 🔐 Authentication System
- ✅ Secure user registration and login
- ✅ Password-protected accounts
- ✅ Session management
- ✅ User profile management

### 👥 Specialist Consultations
- 📅 **Book Expert Sessions** - Schedule one-on-one consultations with certified nutritionists
- ⭐ **Ratings & Reviews** - View specialist ratings and experience
- 🗓️ **Real-time Availability** - See available time slots for the next 7 days
- 💬 **Consultation Notes** - Add specific health concerns and goals
- 📧 **Email Confirmations** - Automatic booking confirmations with payment details

### 🍽️ Meal Plans
- 🥗 **Multiple Diet Types** - Keto, Vegan, Diabetic-Friendly, Balanced, Low-Carb, High-Protein
- 📊 **Nutritional Information** - Detailed calorie and macro breakdowns
- 📅 **Flexible Durations** - 7-day, 14-day, 21-day, and 30-day plans
- 🛒 **Shopping Lists** - Organized ingredient lists (planned feature)
- 👨‍🍳 **Recipe Instructions** - Step-by-step meal preparation guides

### 📚 Health Articles
- 📖 **Educational Content** - Access to comprehensive health articles
- 🏷️ **Categorized** - Nutrition, Fitness, Wellness, Recipes, Health Tips
- 🔍 **Easy Reading** - Modal popups for comfortable reading experience
- 🆓 **Free Access** - Available to all registered users

### 📊 User Dashboard
- 📈 **Purchase History** - View all consultations and meal plan purchases
- 📋 **Booking Management** - Track consultation appointments
- 💰 **Payment Status** - Monitor pending and completed payments
- 📊 **Quick Stats** - Overview of your activity

### 💳 Payment Integration
- 📱 **M-Pesa Integration** - Kenyan mobile money support
- 💵 **Flexible Payment** - Pay for consultations and meal plans separately
- 🧾 **Payment Tracking** - Monitor payment status in dashboard
- 📧 **Payment Instructions** - Clear payment details via email

---

## 🎨 Screenshots

### 🏠 Home Page (Authenticated)
```
┌─────────────────────────────────────────────────┐
│  HEALS        Home  Services▾  My Purchases  👤 │
├─────────────────────────────────────────────────┤
│                                                 │
│   Welcome back, Diana! 👋                       │
│   Continue your journey to healthy living      │
│                                                 │
│   [Book Consultation]  [View Meal Plans]       │
│                                                 │
├─────────────────────────────────────────────────┤
│   Why Choose HEALS                              │
│   📚 Educational  👥 Experts  📅 Personalized   │
├─────────────────────────────────────────────────┤
│   Latest Health Articles                        │
│   [Article 1]  [Article 2]  [Article 3]        │
└─────────────────────────────────────────────────┘
```

### 👨‍⚕️ Specialists Page
```
┌─────────────────────────────────────────────────┐
│        Meet Our Expert Specialists              │
│  Book one-on-one consultations with certified   │
│           nutritionists and wellness coaches    │
├─────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Photo   │  │ Photo   │  │ Photo   │        │
│  │ Dr.Sarah│  │ John K. │  │ Mary W. │        │
│  │ $50/hr  │  │ $45/hr  │  │ $55/hr  │        │
│  │⭐ 4.8   │  │⭐ 4.9   │  │⭐ 5.0   │        │
│  │[Book]   │  │[Book]   │  │[Book]   │        │
│  └─────────┘  └─────────┘  └─────────┘        │
└─────────────────────────────────────────────────┘
```

### 🍽️ Meal Plans Page
```
┌─────────────────────────────────────────────────┐
│         Personalized Meal Plans                 │
│   Choose from expertly crafted meal plans       │
├─────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │ Image   │  │ Image   │  │ Image   │        │
│  │Keto     │  │Balanced │  │Diabetes │        │
│  │Kickstart│  │Living   │  │Care     │        │
│  │7 days   │  │14 days  │  │30 days  │        │
│  │$29      │  │$49      │  │$99      │        │
│  │[Get]    │  │[Get]    │  │[Get]    │        │
│  └─────────┘  └─────────┘  └─────────┘        │
└─────────────────────────────────────────────────┘
```

### 📊 User Dashboard
```
┌─────────────────────────────────────────────────┐
│  My Dashboard                                   │
│  Welcome back, Diana!                           │
├─────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐             │
│  │     3       │  │     2       │             │
│  │Consultations│  │ Meal Plans  │             │
│  └─────────────┘  └─────────────┘             │
├─────────────────────────────────────────────────┤
│  📅 My Consultations                            │
│  ┌──────────────────────────────────────┐     │
│  │ Dr. Sarah Mwangi | Dec 15 | $50 |✓  │     │
│  │ John Kamau       | Dec 20 | $45 |⏳ │     │
│  └──────────────────────────────────────┘     │
├─────────────────────────────────────────────────┤
│  🍽️ My Meal Plans                               │
│  ┌──────────────────────────────────────┐     │
│  │ Keto Kickstart   | 7 days  | $29 |✓ │     │
│  │ Balanced Living  | 14 days | $49 |⏳│     │
│  └──────────────────────────────────────┘     │
└─────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Backend
- **Framework:** Django 5.2
- **Language:** Python 3.12
- **ORM:** Django ORM
- **Database:** SQLite (Development) / PostgreSQL (Production Ready)
- **Authentication:** Django Auth System

### Frontend
- **Framework:** Bootstrap 5.3
- **Icons:** Bootstrap Icons
- **Styling:** Custom CSS with Gradients
- **JavaScript:** Vanilla JS (ES6+)

### Key Libraries
```python
Django==5.2.8
Pillow==10.1.0              # Image handling
django-cors-headers==4.3.0   # CORS support
```

### Features Implemented
- ✅ User Authentication & Authorization
- ✅ Role-based Access Control
- ✅ Email Notifications
- ✅ Payment Tracking System
- ✅ Booking Management
- ✅ File Upload System
- ✅ Responsive Design
- ✅ Admin Dashboard

---

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Step-by-Step Setup

1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/heals-project.git
cd heals-project
```

2️⃣ **Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

4️⃣ **Configure Database**
```bash
python manage.py makemigrations
python manage.py migrate
```

5️⃣ **Create Superuser**
```bash
python manage.py createsuperuser
# Follow the prompts to create admin account
```

6️⃣ **Run Development Server**
```bash
python manage.py runserver
```

7️⃣ **Access the Application**
- **Main Site:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/

---

## 📝 Usage Guide

### For Users

1. **Sign Up**
   - Visit the login page
   - Click "Sign Up"
   - Fill in your details (First Name, Last Name, Username, Email, Password)
   - Click "Create Account"

2. **Browse Specialists**
   - Navigate to "Our Services" → "Specialists"
   - View specialist profiles with ratings and experience
   - Click "Book Consultation" to schedule an appointment

3. **Book a Consultation**
   - Select a specialist
   - Choose an available date and time
   - Fill in your contact details
   - Add any specific notes or concerns
   - Confirm booking
   - Receive email with payment instructions

4. **Purchase Meal Plans**
   - Navigate to "Our Services" → "Meal Plans"
   - Browse available plans
   - Click "Get This Plan"
   - Complete purchase form
   - Receive email with payment details

5. **View Your Dashboard**
   - Click "My Purchases" in the navigation
   - View all consultations and meal plan purchases
   - Track payment status
   - See upcoming appointments

6. **Read Health Articles**
   - Access from the home page after login
   - Click "Read More" on any article
   - Articles open in a modal for easy reading

### For Administrators

1. **Access Admin Panel**
   - Visit http://localhost:8000/admin/
   - Login with superuser credentials

2. **Manage Specialists**
   - Add/Edit specialist profiles
   - Upload photos
   - Set hourly rates and availability

3. **Create Meal Plans**
   - Add new meal plans
   - Set pricing and duration
   - Upload appealing images

4. **Set Specialist Availability**
   - Navigate to "Specialist availabilities"
   - Set working hours for each day of the week
   - Mark available/unavailable slots

5. **Manage Bookings**
   - View all consultation bookings
   - Mark as confirmed or paid
   - Track appointment status

6. **Add Health Articles**
   - Create educational content
   - Categorize by topic
   - Publish for all users

---

## 🗂️ Project Structure
```
heals-project/
│
├── 📁 heals_project/          # Main project directory
│   ├── __init__.py
│   ├── settings.py            # Django settings
│   ├── urls.py                # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
│
├── 📁 core/                   # Main application
│   ├── 📁 migrations/         # Database migrations
│   ├── __init__.py
│   ├── admin.py              # Admin panel configuration
│   ├── apps.py
│   ├── models.py             # Database models
│   ├── views.py              # View functions
│   ├── urls.py               # App URL patterns
│   └── forms.py              # Django forms
│
├── 📁 templates/              # HTML templates
│   ├── home.html             # Public landing page
│   ├── home_authenticated.html # User dashboard
│   ├── login.html            # Login page
│   ├── signup.html           # Registration page
│   ├── specialists.html      # Specialists listing
│   ├── specialist_detail.html # Specialist profile
│   ├── meal-plans.html       # Meal plans listing
│   ├── purchase_meal_plan.html # Purchase form
│   ├── my_purchases.html     # User dashboard
│   ├── booking_confirmation.html
│   └── purchase_confirmation.html
│
├── 📁 static/                 # Static files
│   ├── 📁 css/
│   ├── 📁 js/
│   └── 📁 images/
│
├── 📁 media/                  # User uploaded files
│   ├── 📁 specialists/
│   ├── 📁 meal-plans/
│   └── 📁 articles/
│
├── 📄 manage.py               # Django management script
├── 📄 requirements.txt        # Python dependencies
├── 📄 db.sqlite3             # SQLite database
├── 📄 README.md              # This file
└── 📄 .gitignore             # Git ignore file
```

---

## 🗄️ Database Schema

### Core Models

**User** (Django Built-in)
- username, email, password
- first_name, last_name
- is_active, is_staff

**Specialist**
```python
- name: CharField
- title: CharField (e.g., "Clinical Nutritionist")
- bio: TextField
- years_experience: IntegerField
- hourly_rate: DecimalField
- photo: ImageField
- rating: FloatField (0-5)
- available: BooleanField
```

**MealPlan**
```python
- name: CharField
- description: TextField
- diet_type: CharField (Keto, Vegan, etc.)
- duration: CharField (e.g., "7 days")
- calories: IntegerField
- price: DecimalField
- image: ImageField
```

**Article**
```python
- title: CharField
- content: TextField
- category: CharField
- image: ImageField
- created_at: DateTimeField
```

**Booking**
```python
- user: ForeignKey(User)
- specialist: ForeignKey(Specialist)
- name, email, phone: CharField/EmailField
- booking_date: DateField
- booking_time: TimeField
- status: CharField (PENDING, CONFIRMED, COMPLETED)
- total_amount: DecimalField
- paid: BooleanField
```

**MealPlanPurchase**
```python
- user: ForeignKey(User)
- meal_plan: ForeignKey(MealPlan)
- name, email, phone: CharField/EmailField
- amount_paid: DecimalField
- status: CharField
- paid: BooleanField
```

**SpecialistAvailability**
```python
- specialist: ForeignKey(Specialist)
- day_of_week: IntegerField (0=Monday, 6=Sunday)
- start_time: TimeField
- end_time: TimeField
- is_available: BooleanField
```

---

## 🎯 Roadmap

### Phase 1: MVP ✅ (Completed)
- [x] User authentication system
- [x] Specialist profiles and booking
- [x] Meal plan purchases
- [x] Health articles
- [x] User dashboard
- [x] Admin panel

### Phase 2: Enhancement 🚧 (In Progress)
- [ ] Payment gateway integration (M-Pesa API)
- [ ] Email notifications (SMTP)
- [ ] Video consultation feature
- [ ] Recipe database
- [ ] Grocery shopping list generator

### Phase 3: Advanced Features 📋 (Planned)
- [ ] Mobile app (React Native)
- [ ] AI meal plan recommendations
- [ ] Progress tracking with charts
- [ ] Community forum
- [ ] Nutrition calculator
- [ ] Meal prep instructions with videos

### Phase 4: Expansion 🌍 (Future)
- [ ] Multi-language support
- [ ] Regional meal plans
- [ ] Insurance integration
- [ ] Corporate wellness programs
- [ ] Wearable device integration

---

## 💰 Business Model

### Revenue Streams

1. **Specialist Consultations**
   - Commission: 20% per consultation
   - Average consultation: $30-50
   - Target: 500 sessions/month

2. **Meal Plan Sales**
   - Direct sales: $29-99 per plan
   - Target: 1,000 plans/month

3. **Corporate Wellness**
   - B2B packages: $500-2,000/month
   - Target: 10 companies in Year 1

4. **Affiliate Marketing**
   - Nutritional supplements
   - Kitchen equipment
   - Projected: $12,000/year

**Year 1 Revenue Target:** $483,000 (~KES 74M)

---

## 👥 Target Audience

### Primary Users
1. **Health-Conscious Individuals** (25-45 years)
   - Middle-class professionals
   - Income: KES 50,000+/month

2. **Chronic Condition Management**
   - Diabetics requiring dietary guidance
   - Individuals with hypertension
   - Weight management seekers

3. **Fitness Enthusiasts**
   - Gym-goers seeking optimal nutrition
   - Athletes requiring performance diets

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
```bash
   git checkout -b feature/AmazingFeature
```
3. **Commit your changes**
```bash
   git commit -m 'Add some AmazingFeature'
```
4. **Push to the branch**
```bash
   git push origin feature/AmazingFeature
```
5. **Open a Pull Request**

### Contribution Guidelines
- Follow PEP 8 style guide for Python code
- Write clear commit messages
- Add tests for new features
- Update documentation as needed

---

## 🐛 Known Issues

- [ ] Email notifications use console backend (needs SMTP setup)
- [ ] Payment integration is mock (M-Pesa integration pending)
- [ ] Mobile responsiveness needs minor adjustments on tablets
- [ ] Specialist availability can't be bulk-imported yet

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- Email: your.email@example.com
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)

---

## 🙏 Acknowledgments

- **Bootstrap Team** - For the amazing UI framework
- **Django Community** - For comprehensive documentation
- **Unsplash** - For free stock images
- **Bootstrap Icons** - For beautiful icons
- **Stack Overflow** - For endless problem-solving support

---

## 📞 Support

Need help? We're here for you!

- 📧 **Email:** support@heals.com
- 📱 **Phone:** +254 700 000 000
- 💬 **Issues:** [GitHub Issues](https://github.com/yourusername/heals-project/issues)
- 📖 **Documentation:** [Wiki](https://github.com/yourusername/heals-project/wiki)

---

## 🌟 Star Us!

If you find this project useful, please consider giving it a ⭐ on GitHub!

---

<div align="center">

**Made with ❤️ for a healthier world**

[⬆ Back to Top](#-heals---healthy-eat-long-span)

</div>
