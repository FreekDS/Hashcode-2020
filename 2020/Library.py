import copy

class Library:
    def __init__(self, book_count: int, signup_time: int, scan_limit: int, id: int):
        self.scan_limit = scan_limit
        self.book_count = book_count
        self.signup_time = signup_time
        self.books = list()
        self.id = id
        self.order = list()

    def add_book(self, book):
        self.books.append(book)

    def add_books(self, books):
        self.books=copy.deepcopy(books)
        self.order=list()

    def get_scan_limit(self):
        return self.scan_limit

    def get_signup_time(self):
        return self.signup_time

    def get_books(self):
        return self.books

    def getviabality(self,bookscores):
        scores=0
        for i in self.books:
            scores+=bookscores[i]

        scores=(scores/len(self.books))*self.scan_limit
        print(scores)
        return scores


    def __str__(self):
        return "id "+str(self.id)+" :"+str(self.book_count)+" "+str(+self.signup_time)+" "+str(self.scan_limit)+" "+str(self.books)

    def get_id(self):
        return self.id



