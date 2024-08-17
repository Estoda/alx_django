from models import Book

new = Book.objects.create(title= 'New Book', author = 'George Orwell', publication_year = 2023)
new_book.save()

book = Book.objects.get(publication_year = 1984)

new_book.title = "Ahmed Amin"
new_book.save()

Book.objects.filter(author = new_book.author).delete()
