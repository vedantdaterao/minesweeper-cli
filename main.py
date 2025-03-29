import random
import os
import re

from rich.table import Table
from rich.box import SQUARE
from rich.prompt import Prompt
from rich import print

mines = list()
matrix = list()

for i in range(9):
    tmp = []
    for x in range(9):
        temp = [0,0]
        tmp.append(temp)
    matrix.append(tmp)


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
        matrix[i[0]][i[1]] = ["*",0] # bomb

def print_matrix():
    print()
    table = Table(title="Minesweeper Cli", show_lines=True, box=SQUARE, padding=(0,2), highlight=True, border_style="#284B63")

    table.add_column("[bold]x\y[/bold]", justify="center")
    for num in range(9):
        table.add_column(f"[bold red]{num}[/bold red]", justify="center")

    for x, i in enumerate(matrix):
        row_data = [f"[bold red]{x}[/bold red]"]
        for x in i:
            if x[1] == "x":
                row_data.extend(f"{x[0]}")
            else:
                row_data.extend(f"■")
        table.add_row(*row_data)
    
    print(table)

def show():
    for i in matrix:
        for x in i:
            if x[1] == 'x':
                print(f'[red]{x[0]}[/red]',end = " ")
            else:
                print(f'[cyan]{x[0]}[/cyan]',end = " ")
        print()

def set_numbers(m):
    for i in m:
        r = i[0]
        c = i[1]
        for x in range(r-1,r+2):
            for y in range(c-1,c+2):
                if 0 <= x <= 8 and 0 <= y <= 8:

                    if matrix[x][y][0] != "*":
                        matrix[x][y][0] +=1

generate_mines()
set_mines(10)
set_numbers(mines)
# initial behaviour

def res(coordinates: list):
    r = coordinates[0] 
    c = coordinates[1]
    if matrix[r][c][0] == "*":
        print("you stepped on mine...")
        show()
        exit(0) 
    elif matrix[r][c][0] > 0:
        matrix[r][c][1] = "x"
        return 

    for x in range(r-1,r+2):
        for y in range(c-1,c+2):
            if 0 <= x <= 8 and 0 <= y <= 8:
                if matrix[x][y][0] == 0 and matrix[x][y][1] != "x":
                    matrix[x][y][1] = "x"
                    # print(x,y)
                    res([x,y])

                elif type(matrix[x][y][0]) == int:
                    matrix[x][y][1] = "x"
                    continue
                elif type(matrix[x][y][0]) != int:
                    continue
            else:
                continue


if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear') 
    print_matrix()
    while True:
            coordinates = Prompt.ask(f"Enter coordinates [green](x,y)[/green] or type [green]'exit'[/green] to quit")
            
            if coordinates.lower() == 'exit':
                show()
                exit()

            try:
                x, y = map(int, re.split(r'[,\s]+', coordinates.strip()))
                print(f"coordinates: ({x}, {y})")
                res([x,y])
                os.system('cls' if os.name == 'nt' else 'clear') 
                print_matrix()
            except ValueError:
                print("Invalid input. Please enter coordinates in the format 'x,y'.")
                continue