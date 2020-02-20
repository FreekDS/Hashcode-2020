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

def algorithms(input):
    firsline=input.readline()
    splitted=firsline.split()

    booksAmount=int(splitted[0])
    libraryAmount=int(splitted[1])
    daysAmount=int(splitted[2])
    print("%s %s %s" %(booksAmount,libraryAmount,daysAmount))

    pointslist=list()

    for i in input.readline().split():
        pointslist.append(int(i))
    print(pointslist)

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
        print(i)


    signupVolgorde=orderLibraries(daysAmount,pointslist,libraries)

    outputter =Outputter(libraries)
    outputter.generate_file("./output/"+filename+".txt",list())





if  __name__ == "__main__":
    f=open("./input/"+filename+".txt")
    algorithms(f)


