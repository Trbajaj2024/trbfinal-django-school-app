import os
from django.core.files import File
from django.core.files.images import ImageFile
from main.models import Carousel, Event, Course, Achievement
from django.conf import settings
from PIL import Image
import requests
from io import BytesIO

def add_demo_images():
    # Create media directories if they don't exist
    for directory in ['carousel', 'events', 'courses', 'achievements']:
        os.makedirs(os.path.join(settings.MEDIA_ROOT, directory), exist_ok=True)

    # Sample image URLs (replace with actual image URLs or local images)
    image_urls = {
        'carousel': {
            'welcome.jpg': 'https://example.com/welcome.jpg',
            'facilities.jpg': 'https://example.com/facilities.jpg',
            'faculty.jpg': 'https://example.com/faculty.jpg',
        },
        'events': {
            'science_fair.jpg': 'https://example.com/science_fair.jpg',
            'cultural_fest.jpg': 'https://example.com/cultural_fest.jpg',
            'sports_day.jpg': 'https://example.com/sports_day.jpg',
        },
        'courses': {
            'math.jpg': 'https://example.com/math.jpg',
            'cs.jpg': 'https://example.com/cs.jpg',
            'env_science.jpg': 'https://example.com/env_science.jpg',
        },
        'achievements': {
            'science_olympiad.jpg': 'https://example.com/science_olympiad.jpg',
            'sports_championship.jpg': 'https://example.com/sports_championship.jpg',
            'academic_award.jpg': 'https://example.com/academic_award.jpg',
        }
    }

    # Create placeholder images
    for category, images in image_urls.items():
        for filename, url in images.items():
            # Create a simple placeholder image
            img = Image.new('RGB', (800, 600), color=(73, 109, 137))
            img_io = BytesIO()
            img.save(img_io, format='JPEG')
            img_io.seek(0)

            # Save the image
            file_path = os.path.join(settings.MEDIA_ROOT, category, filename)
            with open(file_path, 'wb') as f:
                f.write(img_io.getvalue())

            # Update the model instances
            if category == 'carousel':
                carousel = Carousel.objects.filter(image__endswith=filename).first()
                if carousel:
                    carousel.image.save(filename, File(open(file_path, 'rb')))
            elif category == 'events':
                event = Event.objects.filter(image__endswith=filename).first()
                if event:
                    event.image.save(filename, File(open(file_path, 'rb')))
            elif category == 'courses':
                course = Course.objects.filter(image__endswith=filename).first()
                if course:
                    course.image.save(filename, File(open(file_path, 'rb')))
            elif category == 'achievements':
                achievement = Achievement.objects.filter(image__endswith=filename).first()
                if achievement:
                    achievement.image.save(filename, File(open(file_path, 'rb')))

if __name__ == '__main__':
    add_demo_images() 