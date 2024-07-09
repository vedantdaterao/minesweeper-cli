import random

mines = list()
matrix = list()



for i in range(9):
    temp = [0] * 9
    matrix.append(temp)

mine_col =1
mine_row = 1


def generate_mines():
    mine = [random.randint(1,8),random.randint(1,8)]
    if mine not in mines:
        return mine
    else:
        return generate_mines()
    

def set_mines(num: int):
    for i in range(num):
        mine = generate_mines()
        mines.append(mine)
    for i in mines:
        print(i)
        matrix[i[0]][i[1]] = "💣"



def print_matrix():
    r = 30
    c = 30
    for i in matrix:
        for j in i:
            # if type(j) == int :
            if type(j) == int:
                    print(" \u25A0 ",end= "")
            else:
                print(j,end= " ")

        print()


def set_numbers(mine):
    for i in mine:
        row = i[0]
        col = i[1]
        pos_rowi,pos_rowd = row -1 , row+1
        pos_coli,pos_cold = col -1 , col+1
        for j in range(pos_rowi,pos_rowd+1):
            for k in range(pos_coli,pos_cold+1):
                if 0 <= j <= 8 and 0 <= k <= 8:
                    if matrix[j][k] != "💣":
                        matrix[j][k] +=1

generate_mines()
set_mines(10)
print(mines)
set_numbers(mines)

# initial behaviour
init_coordinate = [0,0]

def res(coordinates: list):
    row = coordinates[0]
    col = coordinates[1]
    pos_rowi,pos_rowd = row -1 , row+1
    pos_coli,pos_cold = col -1 , col+1
    for j in range(pos_rowi,pos_rowd+1):
        for k in range(pos_coli,pos_cold+1):
            if 0 <= j <= 8 and 0 <= k <= 8:
                if matrix[j][k] == 0:
                    matrix[j][k] = "x"
                    # print(j,k)
                    res([j,k])
                elif matrix[j][k] == int:
                    continue
                elif type(matrix[j][k]) != int:
                    continue
print_matrix()
print()
res(init_coordinate)
print_matrix()