from django.db import migrations

def create_book_data(apps, schema_editor):
    Book = apps.get_model('books', 'Book')
    Book.objects.bulk_create([
        Book(title='To Kill a Mockingbird', author='Harper Lee', publication_date='1960-07-11'),
        Book(title='1984', author='George Orwell', publication_date='1949-06-08'),
        Book(title='Pride and Prejudice', author='Jane Austen', publication_date='1813-01-28'),
        Book(title='The Great Gatsby', author='F. Scott Fitzgerald', publication_date='1925-04-10'),
        Book(title='The Catcher in the Rye', author='J.D. Salinger', publication_date='1951-07-16'),
    ])

class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_book_data),
    ]