# project/urls.py
from django.urls import path
from books.views import export_books_csv, export_books_pdf
from . import views

urlpatterns = [
    path('export_books/', views.export_books, name='export_books'),
    path('books/export/csv/', export_books_csv, name='export_books_csv'),
    path('books/export/pdf/', export_books_pdf, name='export_books_pdf'),
]