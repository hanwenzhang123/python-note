
doctest - A test written in a docstring.
doctest library - The built-in Python library for running doctests.
-m tells the python to download the doctest module, and doctest module will look the file and find the doctest and run it
leave a blank line at the end of your doctest before the closing quotes

# Running doctests
# From the command line
python -m doctest your_script.py

# From inside a script
import doctest
doctest.testmod()



#exercise
#Add a doctest to average() that tests the function with the list [1, 2].
def average(num_list):
    '''Return the average for a list of numbers

    >>> average([1, 2])  # <-- added space after prompt
    1.5

    '''
    return sum(num_list) / len(num_list)


'''dungeon game
explore a dungeon to find a hidden door an escape, but be careful
the grue is hinding somewhere inside!

created: 2014
updated: 2015
Author: Kenneth Love
'''
import os
import random

GAME_DIMENSIONS = (5, 5)
player = {'location': None, 'path': []}


def clear():
  '''clear the screen'''
    os.system('cls' if os.name == 'nt' else 'clear')


def build_cells(width, height):
  '''create and return a 'width' x 'height' grid of two-tuples
  
  >>>  cells = build_cells(2, 2)
  >>>  len(cells)
  4
  
  '''
    cells = []
    for y in range(height):
        for x in range(width):
            cells.append((x, y))
    return cells


def get_locations(cells):
  '''randomly pick starting location for the monster, 
     the door and the player
     
     >>> cells = build_cells(2, 2)
     >>> m, d, p = get_location(cells)
     >>> m != d and d != p
     True
     >>> d in cells
     True
  
  '''
    monster = random.choice(cells)
    door = random.choice(cells)
    player = random.choice(cells)     #recursive function

    if monster == door or monster == player or door == player:
        monster, door, player = get_locations(cells)

    return monster, door, player


def get_moves(player):
    '''based on the tuple of the player's position, return the list
    of acceptable moves
    
    >>> from dd_game import get_moves
    >>> GAME_DIMENSIONS = (2, 2)
    >>> get_moves((0, 2))
    ['RIGHT', 'UP', 'DOWN']
    
    '''
    x, y = player
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    if x == 0:
        moves.remove('LEFT')
    if x == GAME_DIMENSIONS[0] - 1:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == GAME_DIMENSIONS[1] - 1:
        moves.remove('DOWN')
    return moves


def move_player(player, move):
    x, y = player['location']
    player['path'].append((x, y))
    if move == 'LEFT':
        x -= 1
    elif move == 'UP':
        y -= 1
    elif move == 'RIGHT':
        x += 1
    elif move == 'DOWN':
        y += 1
    return x, y


def draw_map(cells):
    print(' _'*GAME_DIMENSIONS[0])
    row_end = GAME_DIMENSIONS[0]
    tile = '|{}'
    for index, cell in enumerate(cells):
        if index % row_end < row_end - 1:
            if cell == player['location']:
                print(tile.format('X'), end='')
            elif cell in player['path']:
                print(tile.format('.'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player['location']:
                print(tile.format('X|'))
            elif cell in player['path']:
                print(tile.format('.|'))
            else:
                print(tile.format('_|'))

def play():
    cells = build_cells(*GAME_DIMENSIONS)
    monster, door, player['location'] = get_locations(cells)

    while True:
        clear()

        print("WELCOME TO THE DUNGEON!")
        moves = get_moves(player['location'])

        draw_map(cells)

        print("\nYou're currently in room {}".format(player['location']))
        print("\nYou can move {}".format(', '.join(moves)))
        print("Enter QUIT to quit")

        move = input("> ")
        move = move.upper()

        if move in ['QUIT', 'Q']:
            break

        if move not in moves:
            print("\n** Walls are hard! Stop running into them! **\n")
            continue

        player['location'] = move_player(player, move)

        if player['location'] == door:
            print("\n** You escaped! **\n")
            break
        elif player['location'] == monster:
            print("\n** You got eaten! **\n")
            break

if __name__ == '__main__':
    play()
   
    
   
