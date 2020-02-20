print(r"""
     ______________________________
    |                              | 
    | THE SQUARE SHEEP VAN ONS MOE | 
    |  -- Google Hashcode 2020 --  |
    |______________________________|

                     ,@;@,
        ,@;@;@;@;@;@/ )@;@;     _ _ _
      ,;@;@;@;@;@;@|_/@o o\    /      \
     (|@;@:@\@;@;@;@:@(   _\  < BAAAA |
     | '@;@;@|@;@;@;@;'`"--'   \_ _ _ / 
     |  '@;@;/;@;/;@;'              
         ) //   | ||         
         \ \\   | ||        
          \ \\  ) \\        -*-     O 
 ----------`"`  `"``--------\|/----\|/-----

""")
# filename="a_example"
# filename="b_read_on"
filename="c_incunabula"
# filename="d_tough_choices"
# filename="e_so_many_books"
# filename="f_libraries_of_the_world"
from Library import *
from Outputgenerator import *

def orderLibraries(daysamount,pointsamount,libraries):
    signupVolgorde=list()
    for i in libraries:
        signupVolgorde.append(i)
    return signupVolgorde


def orderLibraries2(day_count, book_points, libaries: list):
    libaries.sort(key=lambda lib: lib.get_signup_time())

    count = 0
    result = list()
    for lib in libaries:
        lib.books.sort(key=lambda book: book_points[book], reverse=True)
        count += lib.get_signup_time()
        if count >= day_count:
            break

        book_counter = 0
        while book_counter < lib.get_scan_limit():
            lib.order.append(lib.books[book_counter])
            book_counter += 1

        result.append(lib)
        print(lib)

    return result


def algorithms(input):
    firsline=input.readline()
    splitted=firsline.split()

    booksAmount=int(splitted[0])
    libraryAmount=int(splitted[1])
    daysAmount=int(splitted[2])
    #print("%s %s %s" %(booksAmount,libraryAmount,daysAmount))

    pointslist=list()

    for i in input.readline().split():
        pointslist.append(int(i))
    #print(pointslist)

    libraries=list()
    line=f.readline()
    counter = 0
    while line!="" and line!="\n":

        split=line.split()
        templist = list()
        a=int(split[0])
        b=int(split[1])
        c=int(split[2])
        library = Library(a,b,c,counter)
        line=f.readline()
        templist=list()
        for i in line.split():
            templist.append(int(i))
        library.add_books(templist)
        libraries.append(library)
        line=f.readline()
        counter+=1
    for i in libraries:
        pass
        #print(i)


    signupVolgorde=orderLibraries2(daysAmount,pointslist,libraries)

    outputter = Outputter(signupVolgorde)
    outputter.generate_file("./output/"+filename+".txt",list())





if  __name__ == "__main__":
    f=open("./input/"+filename+".txt")
    algorithms(f)