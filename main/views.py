from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Carousel, Program, Event, LiveClass, Course, Achievement, AdmissionApplication, Faculty, AcademicCalendarEvent
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from .forms import AdmissionForm, ContactForm
from django.db import transaction
from django.contrib import messages
import traceback

def home(request):
    """Displays the homepage with dynamic content from the database."""
    now = timezone.now()

    context = {
        # Fetch all active carousels, ordered as specified in the model Meta
        'carousels': Carousel.objects.all(),

        # Fetch programs marked as featured
        'featured_programs': Program.objects.filter(is_featured=True),

        # Fetch the next 3 upcoming events (future dates)
        'upcoming_events': Event.objects.filter(date__gte=now).order_by('date')[:3],

        # Fetch the next 3 upcoming live classes (future dates/times)
        'live_classes': LiveClass.objects.filter(date__gte=now).order_by('date')[:3],

        # Fetch the first 3 featured courses
        'courses': Course.objects.filter(is_featured=True)[:3],

        # Fetch the 3 most recent achievements
        'achievements': Achievement.objects.order_by('-date')[:3],

        # Note: Statistics section was commented out in home.html, so no model/query for it yet.
    }
    return render(request, 'main/home.html', context)

def course_detail(request, pk):
    """Display details of a specific course."""
    course = get_object_or_404(Course, pk=pk)
    context = {
        'page_title': course.title,
        'course': course,
    }
    return render(request, 'main/course_detail.html', context)

def event_list(request):
    """Display all events."""
    now = timezone.now()
    upcoming_events = Event.objects.filter(date__gte=now).order_by('date')
    past_events = Event.objects.filter(date__lt=now).order_by('-date')
    context = {
        'page_title': 'Events',
        'upcoming_events': upcoming_events,
        'past_events': past_events,
    }
    return render(request, 'main/event_list.html', context)

def achievement_list(request):
    """Display all achievements."""
    achievements = Achievement.objects.all().order_by('-date')
    context = {
        'page_title': 'Our Achievements',
        'achievements': achievements,
    }
    return render(request, 'main/achievement_list.html', context) 

def faculty_list(request):
    """Display all faculty members."""
    faculty = Faculty.objects.all().order_by('name')
    context = {
        'page_title': 'Our Faculty',
        'faculty': faculty,
    }
    return render(request, 'main/faculty_list.html', context)

def academic_calendar(request):
    """Display the academic calendar with events grouped by month."""
    events = AcademicCalendarEvent.objects.all().order_by('start_date')
    context = {
        'page_title': 'Academic Calendar',
        'events': events,
    }
    return render(request, 'main/academic_calendar.html', context)

def contact(request):
    """Handle contact form."""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Send email
                send_mail(
                    subject=f"Contact Form: {form.cleaned_data['subject']}",
                    message=f"From: {form.cleaned_data['name']} ({form.cleaned_data['email']})\n\n{form.cleaned_data['message']}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                )
                messages.success(request, 'Your message has been sent successfully!')
                form = ContactForm()  # Clear the form
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
                print(f"Error sending email: {e}")
                print(traceback.format_exc())
    else:
        form = ContactForm()

    context = {
        'page_title': 'Contact Us',
        'form': form,
    }
    return render(request, 'main/contact.html', context)

def course_list(request):
    """Display all courses."""
    courses = Course.objects.all()
    context = {
        'page_title': 'Our Courses',
        'courses': courses,
    }
    return render(request, 'main/course_list.html', context)

def admissions(request):
    """Handle admission form submissions."""
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    application = form.save()
                    # Send confirmation email
                    send_mail(
                        subject="Application Received - Sajan Bajaj Shiksha Sankul",
                        message=f"Dear {application.first_name},\n\nThank you for submitting your application. We will review it and get back to you soon.\n\nBest regards,\nAdmissions Team",
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        recipient_list=[application.email],
                    )
                messages.success(request, 'Your application has been submitted successfully!')
                form = AdmissionForm()  # Clear the form
            except Exception as e:
                messages.error(request, 'An error occurred while submitting your application. Please try again later.')
                print(f"Error processing application: {e}")
                print(traceback.format_exc())
    else:
        form = AdmissionForm()

    context = {
        'page_title': 'Admissions',
        'form': form,
    }
    return render(request, 'main/admissions.html', context) 