from django.db import migrations
from django.utils import timezone
from datetime import timedelta

def add_demo_data(apps, schema_editor):
    # Get models
    Carousel = apps.get_model('main', 'Carousel')
    Program = apps.get_model('main', 'Program')
    Event = apps.get_model('main', 'Event')
    LiveClass = apps.get_model('main', 'LiveClass')
    Course = apps.get_model('main', 'Course')
    Achievement = apps.get_model('main', 'Achievement')

    # Add Carousel items
    carousel_data = [
        {
            'title': 'Welcome to TRBSS',
            'subtitle': 'Empowering students through quality education',
            'image': 'carousel/welcome.jpg',
            'order': 0
        },
        {
            'title': 'State-of-the-Art Facilities',
            'subtitle': 'Modern classrooms and advanced learning resources',
            'image': 'carousel/facilities.jpg',
            'order': 1
        },
        {
            'title': 'Expert Faculty',
            'subtitle': 'Learn from experienced and dedicated teachers',
            'image': 'carousel/faculty.jpg',
            'order': 2
        }
    ]

    for data in carousel_data:
        Carousel.objects.create(**data)

    # Add Programs
    program_data = [
        {
            'title': 'Science Program',
            'icon': 'fas fa-flask',
            'description': 'Comprehensive science education with practical experiments and research opportunities.',
            'is_featured': True
        },
        {
            'title': 'Arts Program',
            'icon': 'fas fa-palette',
            'description': 'Creative arts program focusing on visual and performing arts.',
            'is_featured': True
        },
        {
            'title': 'Sports Program',
            'icon': 'fas fa-running',
            'description': 'Professional sports training with state-of-the-art facilities.',
            'is_featured': True
        }
    ]

    for data in program_data:
        Program.objects.create(**data)

    # Add Events
    event_data = [
        {
            'title': 'Annual Science Fair',
            'image': 'events/science_fair.jpg',
            'date': timezone.now() + timedelta(days=30),
            'description': 'Join us for our annual science fair showcasing student projects and innovations.'
        },
        {
            'title': 'Cultural Festival',
            'image': 'events/cultural_fest.jpg',
            'date': timezone.now() + timedelta(days=45),
            'description': 'Celebrate our diverse culture with performances, food, and art exhibitions.'
        },
        {
            'title': 'Sports Day',
            'image': 'events/sports_day.jpg',
            'date': timezone.now() + timedelta(days=60),
            'description': 'Annual sports day with various competitions and fun activities.'
        }
    ]

    for data in event_data:
        Event.objects.create(**data)

    # Add Live Classes
    live_class_data = [
        {
            'title': 'Mathematics Masterclass',
            'description': 'Advanced mathematics concepts and problem-solving techniques.',
            'date': timezone.now() + timedelta(days=2),
            'link': 'https://example.com/math-class'
        },
        {
            'title': 'Science Lab Session',
            'description': 'Interactive science experiments and demonstrations.',
            'date': timezone.now() + timedelta(days=5),
            'link': 'https://example.com/science-lab'
        },
        {
            'title': 'Creative Writing Workshop',
            'description': 'Learn creative writing techniques and storytelling.',
            'date': timezone.now() + timedelta(days=7),
            'link': 'https://example.com/writing-workshop'
        }
    ]

    for data in live_class_data:
        LiveClass.objects.create(**data)

    # Add Courses
    course_data = [
        {
            'title': 'Advanced Mathematics',
            'image': 'courses/math.jpg',
            'description': 'Comprehensive course covering advanced mathematical concepts and applications.',
            'is_featured': True
        },
        {
            'title': 'Computer Science',
            'image': 'courses/cs.jpg',
            'description': 'Introduction to programming, algorithms, and computer systems.',
            'is_featured': True
        },
        {
            'title': 'Environmental Science',
            'image': 'courses/env_science.jpg',
            'description': 'Study of environmental systems and sustainable practices.',
            'is_featured': True
        }
    ]

    for data in course_data:
        Course.objects.create(**data)

    # Add Achievements
    achievement_data = [
        {
            'title': 'National Science Olympiad Winners',
            'image': 'achievements/science_olympiad.jpg',
            'date': timezone.now() - timedelta(days=90),
            'description': 'Our students secured top positions in the National Science Olympiad.'
        },
        {
            'title': 'Sports Championship',
            'image': 'achievements/sports_championship.jpg',
            'date': timezone.now() - timedelta(days=60),
            'description': 'School team won the regional sports championship.'
        },
        {
            'title': 'Academic Excellence Award',
            'image': 'achievements/academic_award.jpg',
            'date': timezone.now() - timedelta(days=30),
            'description': 'Recognized for outstanding academic performance and innovation.'
        }
    ]

    for data in achievement_data:
        Achievement.objects.create(**data)

def remove_demo_data(apps, schema_editor):
    # Get models
    Carousel = apps.get_model('main', 'Carousel')
    Program = apps.get_model('main', 'Program')
    Event = apps.get_model('main', 'Event')
    LiveClass = apps.get_model('main', 'LiveClass')
    Course = apps.get_model('main', 'Course')
    Achievement = apps.get_model('main', 'Achievement')

    # Remove all demo data
    Carousel.objects.all().delete()
    Program.objects.all().delete()
    Event.objects.all().delete()
    LiveClass.objects.all().delete()
    Course.objects.all().delete()
    Achievement.objects.all().delete()

class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_demo_data, remove_demo_data),
    ] 