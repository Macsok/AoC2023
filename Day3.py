def part1():
    whole_file = open('input.txt').readlines()  #   whole_file[0] - one row
    numb = ''
    sum = 0

    for y in range(0, len(whole_file)):
        good = False
        for x in range(0, len(whole_file[y])):

            x_edge = len(whole_file[y]) - 1
            y_edge = len(whole_file) - 1

            if whole_file[y][x].isdigit():
                #print(int(whole_file[y][x]))
                numb += whole_file[y][x]
                #   cases
                if not good:
                    if y != 0:
                        if whole_file[y - 1][x] != '.' and not whole_file[y - 1][x].isdigit():
                            #print("not good")
                            good = True
                    if y != 0 and x != 0:
                        if whole_file[y - 1][x - 1] != '.' and not whole_file[y - 1][x - 1].isdigit():
                            good = True
                    if y != 0 and x != x_edge:
                        if whole_file[y - 1][x + 1] != '.' and not whole_file[y - 1][x + 1].isdigit():
                            good = True
                    if x != 0:
                        if whole_file[y][x - 1] != '.' and not whole_file[y][x - 1].isdigit():
                            good = True
                    if x != x_edge:
                        if whole_file[y][x + 1] != '.' and not whole_file[y][x + 1].isdigit():
                            good = True
                    if y != y_edge and x != 0:
                        if whole_file[y + 1][x - 1] != '.' and not whole_file[y + 1][x - 1].isdigit():
                            good = True
                    if y != y_edge:
                        if whole_file[y + 1][x] != '.' and not whole_file[y + 1][x].isdigit():
                            good = True
                    if y != y_edge and x != x_edge:
                        if whole_file[y + 1][x + 1] != '.' and not whole_file[y + 1][x + 1].isdigit():
                            good = True
                #   end of cases
            else:
                if good and numb != '':
                    #print(numb)
                    sum += int(numb)
                numb = ''
                good = False
            if x == x_edge:
                if good and numb != '':
                    sum += int(numb)
                numb = ''
                good = False
    print(sum)