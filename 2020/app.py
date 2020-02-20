import random

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

files = ["a_example", "b_read_on", "c_incunabula", "d_tough_choices", "e_so_many_books", "f_libraries_of_the_world"]
disable = False

#filename="a_example"
#filename="b_read_on"
#filename="c_incunabula"
#filename="d_tough_choices"
#filename="e_so_many_books"
filename="f_libraries_of_the_world"

from Library import *
from Outputgenerator import *


def orderLibraries(daysamount, pointsamount, libraries):
    libraries.sort(key=lambda lib: ((len(lib.books) / lib.get_scan_limit()) / lib.get_signup_time()), reverse=True)
    # order libraries in groups per signup time
    # libraries_per_signup_time = list()
    # for i in libraries:
    #     time = i.get_signup_time()
    #     assigned = False
    #     for signupTime_lib in libraries_per_signup_time:
    #         if signupTime_lib[0] == time:
    #             signupTime_lib[1].append(i)
    #             assigned = True
    #             break
    #     if assigned == False:
    #         libraries_per_signup_time.append([i.get_signup_time(), [i]])
    #
    # # order libraries in groups by
    # for signupTime_lib in libraries_per_signup_time:
    #     signupTime_lib[1].sort(key=lambda lib: lib.get_scan_limit())
    #
    # libraries_per_signup_time.sort(key=lambda iter: iter[0])
    #
    # # actually put everything in one list
    # signupVolgorde = list()
    # for signupTime_lib in libraries_per_signup_time:
    #     for lib in signupTime_lib[1]:
    #         signupVolgorde.append(lib)

    return libraries


def orderLibraries2(day_count, book_points, libaries: list):
    libaries = orderLibraries(day_count, book_points, libaries)
    # libaries.sort(key=lambda lib: lib.getviabality(book_points))
    count = 0
    result = list()
    for lib in libaries:
        lib.books.sort(key=lambda book: book_points[book], reverse=True)
        count += lib.get_signup_time()
        if count >= day_count:
            break

        book_counter = 0
        # while book_counter < lib.get_scan_limit()*():
        while True:
            if book_counter >= len(lib.books):
                break
            lib.order.append(lib.books[book_counter])
            book_counter += 1

        result.append(lib)
        # print(lib)

    return result


def algorithms(input,fileke):
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
    outputter.generate_file("./output/"+fileke+".txt",list())


if  __name__ == "__main__":
    if disable:
        with open("./input/"+filename+".txt") as f:
            algorithms(f,filename)
    else:
        for file in files:
            with open("./input/"+file+".txt") as f:
                algorithms(f,file)



