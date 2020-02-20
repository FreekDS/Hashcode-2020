from Book import Book


class Library:
    def __init__(self, book_count, signup_time, scan_limit):
        self.scan_limit = scan_limit
        self.book_count = book_count
        self.signup_time = signup_time
        self.books = list()

    def add_book(self, book):
        self.books.append(book)

    def add_books(self, books):
        self.books=(books)

    def get_scan_limit(self):
        return self.scan_limit

    def get_signup_time(self):
        return self.signup_time

    def get_books(self):
        return self.books

    def __str__(self):
        return str(self.book_count)+" "+str(+self.signup_time)+" "+str(self.scan_limit)+" "+str(self.books)