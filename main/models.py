from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Carousel(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image = models.ImageField(upload_to='carousel/')
    order = models.PositiveIntegerField(default=0, help_text="Lower numbers display first.")

    class Meta:
        ordering = ['order', 'title']

    def __str__(self):
        return self.title

class Program(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="e.g., 'fas fa-book'. Use Font Awesome class names.")
    description = models.TextField()
    is_featured = models.BooleanField(default=False, help_text="Check to display on the homepage.")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/')
    date = models.DateTimeField()
    description = models.TextField()

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title

class LiveClass(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    link = models.URLField()

    class Meta:
        ordering = ['date']
        verbose_name = "Live Class"
        verbose_name_plural = "Live Classes"

    def __str__(self):
        return self.title

class Course(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='courses/', blank=True, null=True)
    description = models.TextField()
    is_featured = models.BooleanField(default=False, help_text="Check to display on the homepage featured section.")

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='achievements/', blank=True, null=True)
    date = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ['-date'] # Show most recent first

    def __str__(self):
        return self.title

class AdmissionApplication(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    previous_school = models.CharField(max_length=200)
    grade_applying_for = models.CharField(max_length=50)
    parent_name = models.CharField(max_length=200)
    parent_occupation = models.CharField(max_length=200)
    parent_email = models.EmailField()
    parent_phone = models.CharField(max_length=15)
    additional_notes = models.TextField(blank=True)
    application_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending', choices=[
        ('Pending', 'Pending'),
        ('Under Review', 'Under Review'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected')
    ])

    class Meta:
        ordering = ['-application_date']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.grade_applying_for}"

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    qualification = models.CharField(max_length=200)
    experience = models.PositiveIntegerField(help_text="Years of experience")
    image = models.ImageField(upload_to='faculty/', blank=True, null=True)
    bio = models.TextField()
    email = models.EmailField()
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(r'^\d{10}$', 'Enter a valid 10-digit phone number.')],
        blank=True
    )
    specialization = models.CharField(max_length=200)
    achievements = models.TextField(blank=True)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Order of appearance")

    class Meta:
        verbose_name_plural = "Faculty Members"
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} - {self.designation}"

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.subject} - {self.name}"

class AcademicCalendarEvent(models.Model):
    EVENT_TYPE_CHOICES = [
        ('holiday', 'Holiday'),
        ('exam', 'Examination'),
        ('event', 'School Event'),
        ('activity', 'Activity'),
        ('other', 'Other')
    ]
    
    title = models.CharField(max_length=200)
    event_type = models.CharField(max_length=20, choices=EVENT_TYPE_CHOICES, default='other')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    is_important = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['start_date']
        
    def __str__(self):
        return self.title 