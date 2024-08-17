from relationship_app.models import Author, Book, Library, Librarian
books = Book.objects.all()
for book in books:
    if book.author.name == "Ahmed Amin":
        print(book)

library = Library.objects.get(name = "Cairo")
books = library.books.all()

for book in books:
    print(book)

librarians = Librarian.objects.all()
for librarian in librarians:
    if librarians.library == Library.objects.get(name = "Cairo"):
        print(librarian)
