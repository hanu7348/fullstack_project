import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fullstack_project.settings')

import django
django.setup()

from books.models import Book

Book.objects.bulk_create([
    Book(title='To Kill a Mockingbird', author='Harper Lee', publication_date='1960-07-11'),
    Book(title='1984', author='George Orwell', publication_date='1949-06-08'),
    Book(title='Pride and Prejudice', author='Jane Austen', publication_date='1813-01-28'),
    Book(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_date='1925-04-10'),
    Book(title='The Catcher in the Rye', author='J.D. Salinger', publication_date='1951-07-16'),
])