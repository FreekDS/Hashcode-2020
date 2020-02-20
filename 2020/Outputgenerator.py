

class Outputter:
    def __init__(self, libraries: list):
        self.libraries = libraries

    def set_libraries(self, libraries):
        self.libraries = libraries

    def clear_libraries(self):
        self.libraries.clear()

    def add_library(self, library):
        self.libraries.append(library)

    def generate_file(self, filename, all_books):
        with open(filename, 'w') as file:
            file.write(str(len(self.libraries)))    # lib count
            for lib in self.libraries:
                file.write(str(lib.get_id()) + " " + str(len(lib.books)))   # lib id + book amount
                line = str()
                for book in lib.books:
                    line += str(book) + " "
                file.write(line)    # if scoring complains of whitespaces, remove last char of line (is whitespace
