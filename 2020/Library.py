from Book import Book


class Library:
    def __init__(self, book_count, signup_time, scan_limit):
        self.scan_limit = scan_limit
        self.book_count = book_count
        self.signup_time = signup_time
        self.books = list()

    def add_book(self, book: Book):
        self.books.append(book)

    def get_scan_limit(self):
        return self.scan_limit

    def get_signup_time(self):
        return self.signup_time

    def get_books(self):
        return self.books