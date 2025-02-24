

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
            file.write(str(len(self.libraries)))  # lib count
            file.write("\n")
            for lib in self.libraries:
                if(len(lib.order)):
                    file.write(str(lib.get_id()) + " " + str(len(lib.order)))   # lib id + book amount
                    file.write("\n")
                    line = str()
                    for book in lib.order:
                        line += str(book) + " "
                    file.write(line)    # if scoring complains of whitespaces, remove last char of line (is whitespace!=0
                    file.write("\n")
