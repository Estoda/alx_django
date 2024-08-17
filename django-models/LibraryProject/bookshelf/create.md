from models import Book

new = Book.objects.create(title= 'New Book', author = 'George Orwell', publication_year = 2023)
new_book.save()
