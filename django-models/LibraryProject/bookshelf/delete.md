from bookshelf.models import Book
book = Book.objects.filter(author = new_book.author)
book.delete()
