def part1():
    with open('input.txt', mode = 'r') as file:
        sum = 0
        for line in file:
            first = ''
            last = ''
            for one in line:
                if one.isdecimal():
                    last = one
                    if first == '':
                        first = one
            sum += int(first + last)
    print(sum)

import re

def part2():
    with open('input.txt', mode = 'r') as file:
        sum = 0
        for line in file:
            last = -1
            first = len(line)

            dict = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}
            check = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
            for case in check:
                if int(line.find(case)) < first and int(line.find(case)) > -1:
                    first = line.find(case)
                    num1 = dict[case]
                if line.rfind(case) > last:
                    last = line.rfind(case)
                    num2 = dict[case]

            i = 0
            for one in line:
                if one.isdecimal():
                    if i < int(first):
                        first = i
                        num1 = int(one)
                    if i > int(last):
                        print("a")
                        last = i
                        num2 = int(one)
                i += 1
            sum += int(str(num1) + str(num2))
            #print(first, last, num1, num2, int(str(num1)+str(num2)), sum, '\n')
    print(sum)
#part2()
