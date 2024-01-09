# create_initial_data.py

import os
import django
from django.utils import timezone
from myapp.myapp.models import Author, Book, Genre

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
django.setup()

def create_initial_data():
    # Create genres
    fiction = Genre.objects.create(name='Fiction')
    non_fiction = Genre.objects.create(name='Non-Fiction')

    # Create authors
    author1 = Author.objects.create(name='Author 1', bio='Bio of Author 1')
    author2 = Author.objects.create(name='Author 2', bio='Bio of Author 2')

    # Create books
    book1 = Book.objects.create(
        title='Book 1',
        publication_date=timezone.now(),
        author=author1,
        genre=fiction,
        summary='Summary of Book 1',
        isbn='1234567890123',
    )

    book2 = Book.objects.create(
        title='Book 2',
        publication_date=timezone.now(),
        author=author2,
        genre=non_fiction,
        summary='Summary of Book 2',
        isbn='9876543210987',
    )

    print('Initial data created successfully.')

if __name__ == '__main__':
    create_initial_data()
