from django.contrib import admin
from import_export import resources
from .models import (
    Carousel, Program, Event, LiveClass, Course, 
    Achievement, AdmissionApplication, Faculty, AcademicCalendarEvent
)
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
import io
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from import_export.formats import base_formats
from import_export.admin import ImportMixin, ExportMixin
import csv
from django.utils.encoding import smart_str

# Register your models here to make them accessible in the Django admin interface.

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'image')
    list_editable = ('order',)
    search_fields = ('title', 'subtitle')
    list_per_page = 20

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'is_featured')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    list_per_page = 20

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(LiveClass)
class LiveClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'link')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured', 'image')
    list_filter = ('is_featured',)
    search_fields = ('title', 'description')
    list_per_page = 20

@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image')
    list_filter = ('date',)
    search_fields = ('title', 'description')
    date_hierarchy = 'date'
    list_per_page = 20

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'grade_applying_for', 'parent_name', 'application_date', 'status', 'action_buttons')
    list_filter = ('status', 'grade_applying_for', 'application_date')
    search_fields = ('first_name', 'last_name', 'parent_name', 'email', 'parent_email')
    readonly_fields = ('application_date',)
    date_hierarchy = 'application_date'
    actions = ['export_as_csv', 'export_as_pdf']
    
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = 'Student Name'
    
    def action_buttons(self, obj):
        return format_html(
            '<a class="button" href="{}">View</a>&nbsp;'
            '<a class="button" href="{}">Edit</a>',
            f'/admin/main/admissionapplication/{obj.id}/change/',
            f'/admin/main/admissionapplication/{obj.id}/change/'
        )
    action_buttons.short_description = 'Actions'
    
    def export_as_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="admission_applications.csv"'
        writer = csv.writer(response)
        
        # Write headers
        writer.writerow([
            'Student Name',
            'Grade',
            'Parent Name',
            'Contact',
            'Email',
            'Status',
            'Date'
        ])
        
        # Write data
        for obj in queryset:
            writer.writerow([
                smart_str(f"{obj.first_name} {obj.last_name}"),
                smart_str(obj.grade_applying_for),
                smart_str(obj.parent_name),
                smart_str(obj.parent_phone),
                smart_str(obj.parent_email),
                smart_str(obj.status),
                smart_str(obj.application_date.strftime('%Y-%m-%d'))
            ])
        
        return response
    export_as_csv.short_description = "Export selected applications to CSV"
    
    def export_as_pdf(self, request, queryset):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="admission_applications.pdf"'
        
        # Create PDF
        p = canvas.Canvas(response, pagesize=letter)
        width, height = letter
        
        # Add title
        p.setFont("Helvetica-Bold", 16)
        p.drawString(50, height - 50, "Admission Applications")
        
        # Get data
        applications = queryset if queryset else AdmissionApplication.objects.all()
        
        # Create table data
        data = [['Student Name', 'Grade', 'Parent Name', 'Contact', 'Status', 'Date']]
        for app in applications:
            data.append([
                f"{app.first_name} {app.last_name}",
                app.grade_applying_for,
                app.parent_name,
                app.parent_phone,
                app.status,
                app.application_date.strftime('%Y-%m-%d')
            ])
        
        # Create table
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 14),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        
        # Draw table
        table.wrapOn(p, width, height)
        table.drawOn(p, 50, height - 200)
        
        p.showPage()
        p.save()
        return response
    export_as_pdf.short_description = "Export selected applications to PDF"

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'department', 'qualification', 'experience', 'is_active')
    list_filter = ('department', 'is_active', 'joining_date')
    search_fields = ('name', 'designation', 'department', 'qualification')
    ordering = ('order', 'name')
    list_editable = ('is_active',)
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'designation', 'department', 'image')
        }),
        ('Qualifications & Experience', {
            'fields': ('qualification', 'experience', 'specialization')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone')
        }),
        ('Additional Information', {
            'fields': ('bio', 'achievements', 'joining_date')
        }),
        ('Display Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(AcademicCalendarEvent)
class AcademicCalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'start_date', 'end_date', 'is_important')
    list_filter = ('event_type', 'is_important', 'start_date')
    search_fields = ('title', 'description')
    date_hierarchy = 'start_date'
    list_editable = ('is_important',)
    list_per_page = 20 