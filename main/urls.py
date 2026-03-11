from django.urls import path
from . import views

# Define URL patterns for the main app
urlpatterns = [
    # Map the root URL of the app ('/') to the home view
    path('', views.home, name='home'),

    # Example placeholder URLs for views mentioned in home.html
    # You will need to implement these views in views.py
    path('courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('admissions/', views.admissions, name='admissions'),

    # New list pages
    path('courses/', views.course_list, name='course_list'),
    path('events/', views.event_list, name='event_list'),
    path('achievements/', views.achievement_list, name='achievement_list'),
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('academic-calendar/', views.academic_calendar, name='academic_calendar'),
    path('contact/', views.contact, name='contact'),
] 