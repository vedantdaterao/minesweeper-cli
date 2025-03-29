import random 
import copy


mines = list()

matrix = list()

for x in range(9):
    temp = [0]*9
    matrix.append(temp)

def generateMine():
    mine = [random.randint(0,8), random.randint(0,8)]
    if mine not in mines:
        return mine
    else:
        return generateMine()

def setMines(num: int):
    for _ in range(num):
        mine = generateMine()
        mines.append(mine) 
    for i in mines:
        #print(i)
        matrix[i[0]][i[1]] ='💣'

#--------------------------------------|

def setNumbers(mines):
    for i in mines:
        r, c = i
        for x in range(r-1, r+2):
            for y in range(c-1, c+2):
                #print('->', x, y)
                if 0 <= x <= 8 and 0 <= y <= 8:
                    if matrix[x][y] != '💣':
                        matrix[x][y] += 1
#---------------------------------------|

def gameState():
    for x in field:
        for y in x:
            print(' ', y, end=' ')
        print()
    print('game over')
    exit()
#---------------------------------------|

def choose(coord: list):
    r, c = coord

    # if matrix[r][c] == '💣':
    #     gameState()
    # elif matrix[r][c] == 'x':
    #     return
    # elif matrix[r][c] != 0:
    #     matrix[r][c] = 'x'
    #     return
    if matrix[r][c] == 0:
        for x in range(r-1, r+2):
            for y in range(c-1, c+2):
                #print('->', x, y)

                if 0 <= x <= 8 and 0 <= y <= 8:
                    if matrix[x][y] == 0:
                        matrix[x][y] = "x"
                        # print(x,y)
                        choose([x,y])
                    elif matrix[x][y] == int:
                        matrix[x][y] = 'x'
                        continue
                    elif type(matrix[x][y]) != int:
                        continue

    if type(matrix[r][c]) == int:
        matrix[r][c] = 'x'
        
    # if matrix[r][c] == 'x':
    #     return

    if matrix[r][c] == '💣':
        gameState()

                # elif matrix[x][y] ==  int:
                #     # print("i")
                #     breay

                # elif matrix[x][y] == '💣':
                #     gameState()

                

#   0,0 0,1 0,2
#   1,0 1,1 1,2
#   2,0 2,1 2,2

#----------------------------------------------------

def printMatrix():
    for x in range(9):
        for y in range(9):
            if matrix[x][y] == 'x':
                print(field[x][y], end=' ')
            else:
                print(' ■ ', end='')
        print()


    # for i in matrix:
    #     for x in i:
    #         if type(x) == int:
    #             print(' ■ ', end='')
    #         else:
    #             print(x, end=' ')
    #     print()

# print(matrix)
# for i in matrix:
#     print(i)
# print()
# for x in matrix:
#     for y in x:
#         if y == '💣':
#             print(' ■ ', end='')
#         elif y == 0:
#             print(' ■ ', end='')
#         elif y == ' x ':
#             print(' ■ ', end='')
#         elif type(y) == int:
#             print(y, end=' ')
#     print()
             
#----------------------------------------------------


#----------------------------------------------------|
# set mine field
setMines(3)
setNumbers(mines)

field = copy.deepcopy(matrix)

# setcoord = [1,1]
# choose(setcoord)
printMatrix()

while True:
        coordinates = input("Enter coordinates (x, y) or type 'exit' to quit: ")
        
        if coordinates.lower() == 'exit':
            gameState()
            exit()
        
        try:
            x, y = map(int, coordinates.split(','))
            if x & y > 8:
                print("Invalid")
                continue
            print(f"coordinates: ({x}, {y})")
            choose([x,y])
            printMatrix()
        except ValueError:
            print("Invalid input. Please enter coordinates in the format 'x, y'.")
            continue


