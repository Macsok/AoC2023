def part1():
    with open('input.txt') as file:
        sum = 0
        for game in file:
            possible = True
            game_index = int(game.split(' ')[1][:-1])
            
            for hand in game.split(':')[1].split(';'):
                balls = hand.split(',')

                for similar in balls:
                    if similar.find('red') > -1:
                        if int(similar.split(' ')[1]) > 12: possible = False
                    if similar.find('green') > -1:
                        if int(similar.split(' ')[1]) > 13: possible = False
                    if similar.find('blue') > -1:
                        if int(similar.split(' ')[1]) > 14: possible = False
            if possible: sum += game_index
        print(sum)

def part2():
    with open('input.txt') as file:
        sum = 0
        for game in file:
            red_min = 0
            green_min = 0
            blue_min = 0
            
            for hand in game.split(':')[1].split(';'):
                balls = hand.split(',')

                for similar in balls:
                    if similar.find('red') > -1:
                        if int(similar.split(' ')[1]) > red_min:
                            red_min = int(similar.split(' ')[1])
                    if similar.find('green') > -1:
                        if int(similar.split(' ')[1]) > green_min:
                            green_min = int(similar.split(' ')[1])
                    if similar.find('blue') > -1:
                        if int(similar.split(' ')[1]) > blue_min:
                            blue_min = int(similar.split(' ')[1])
            sum += red_min * green_min * blue_min
        print(sum)

part2()