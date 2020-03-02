# Write a method that takes a field for well-known board game "Battleship" as an argument and returns true if it has a valid disposition of ships, false otherwise. Argument is guaranteed to be 10*10 two-dimension array. Elements in the array are numbers, 0 if the cell is free and 1 if occupied by ship.
#
# Battleship (also Battleships or Sea Battle) is a guessing game for two players. Each player has a 10x10 grid containing several "ships" and objective is to destroy enemy's forces by targetting individual cells on his field. The ship occupies one or more cells in the grid. Size and number of ships may differ from version to version. In this kata we will use Soviet/Russian version of the game.
#
#
# Before the game begins, players set up the board and place the ships accordingly to the following rules:
# There must be single battleship (size of 4 cells), 2 cruisers (size 3), 3 destroyers (size 2) and 4 submarines (size 1). Any additional ships are not allowed, as well as missing ships.
# Each ship must be a straight line, except for submarines, which are just single cell.
#
# The ship cannot overlap or be in contact with any other ship, neither by edge nor by corner.


import numpy as np

def count_streak(n,l):
    l = list(l)
    m= [l[0]] + [0 for k in range(len(l)-1)]
    for i in range(1,len(l)):
        if l[i] == 0:
            m[i] = 0
        else:
            m[i] = 1 + m[i-1]
    q = list(m)
    for j in range(len(l)-2,-1,-1):
        if m[j] <= q[j+1]:
            m[j] = 0
    return(m.count(n))

num_battleships = 1
num_cruisers = 2
num_destroyers = 3
num_submarines = 4

Total_size = 20

def validate_battlefield(field):
    battleField = np.array(field)
    for r in range(battleField.shape[0] - 1):
        for c in range(battleField.shape[1] - 1):
            if battleField[r,c] == 1 and battleField[r+1,c+1] == 1:
                return False
        for c in range(1,battleField.shape[1]):
            if battleField[r,c] == 1 and battleField[r+1,c-1] == 1:
                return False

    if sum(sum(battleField[k]) for k in range(len(battleField))) != Total_size:
        return False

    cs_battleship = sum(count_streak(4,battleField[k,:]) for k in range(battleField.shape[0]))\
    + sum(count_streak(4,battleField[:,k]) for k in range(battleField.shape[1]))
    cs_cruisers = sum(count_streak(3,battleField[k,:]) for k in range(battleField.shape[0]))\
    + sum(count_streak(3,battleField[:,k]) for k in range(battleField.shape[1]))
    cs_destroyers = sum(count_streak(2,battleField[k,:]) for k in range(battleField.shape[0]))\
    + sum(count_streak(2,battleField[:,k]) for k in range(battleField.shape[1]))
    cs_submarines = sum(count_streak(1,battleField[k,:]) for k in range(battleField.shape[0]))\
    + sum(count_streak(1,battleField[:,k]) for k in range(battleField.shape[1])) - Total_size

    if cs_battleship != num_battleships or cs_cruisers != num_cruisers\
    or cs_destroyers != num_destroyers or cs_submarines != num_submarines:
        return False

    return True
