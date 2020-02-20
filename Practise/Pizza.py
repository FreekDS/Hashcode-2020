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

files = ["a_example", "b_small", "c_medium", "d_quite_big", "e_also_big"]


def algo(file):
    with open("./input/" + file + ".in" , 'r') as f:
        pizzas = list()
        first_line = f.readline()
        second_line = f.readline()

        max_slices = int(first_line.split(' ')[0])
        type_amount = int(first_line.split(' ')[1])

        sliced = second_line.split(' ')
        for i in range(0, type_amount):
            pizzas.insert(i, int(sliced[i]))

        result = []
        for i in range(len(pizzas) -1, -1, -1):
            if pizzas[i] < max_slices:
                max_slices -= pizzas[i]
                result.append(i)

        out = open("./output/" + file + ".out", 'w')

        out.write(str(len(result)) + "\n")

        line = str()
        for i in reversed(result):
            line += str(i)
            line += " "

        out.write(line)

        out.close()
        f.close()


for file in files:
    algo(file)

