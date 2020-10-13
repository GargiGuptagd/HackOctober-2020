# -*- coding: utf-8 -*-
"""
Created on Fri Jun 28 17:40:00 2019

@author: Mainak
"""

import numpy
board= numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])
p1name=input("Enter player 1 name: ")
p2name=input("Enter player 2 name: ")
print()
p1s='X'
p2s='O'

def check_rows(symbol):
    for r in range(3):
        count=0
        for c in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            if p1s==symbol:
                print(p1name,'Won')
            else:
                print(p2name,'Won')
            return True
    return False

def check_cols(symbol):
    for c in range(3):
        count=0
        for r in range(3):
            if board[r][c]==symbol:
                count+=1
        if count==3:
            if p1s==symbol:
                print(p1name,'Won')
            else:
                print(p2name,'Won')
            return True
    return False

def check_diagonals(symbol):
    if board[0][2]==board[1][1] and board[1][1]==board[2][0] and board[1][1]==symbol:
        if p1s==symbol:
            print(p1name,'Won')
        else:
            print(p2name,'Won')
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[1][1]==symbol:
        if p1s==symbol:
            print(p1name,'Won')
        else:
            print(p2name,'Won')
        return True
    return False
def won(symbol):
    return check_rows(symbol) or check_cols(symbol) or check_diagonals(symbol)

def place(symbol):
    print(numpy.matrix(board))
    while(1):
        row=int(input('Enter row - 1 or 2 or 3: '))
        col=int(input('Enter column - 1 or 2 or 3: '))
        if row>0 and row<4 and col>0 and col<4 and board[row-1][col-1]=='-':
            break
        else:
            print('Invalid input. please enter again')
    board[row-1][col-1]=symbol
   
def play():
    for turn in range(9):
        if turn%2==0:
            print(p1name,'its your turn. Put a X.',end = '\n\n')
            place(p1s)
            if won(p1s):
                break
        else:
            print(p2name,'its your turn. Put a O.',end = '\n\n')
            place(p2s)
            if won(p2s):
                break
    if not(won(p1s)) and not(won(p2s)):
        print('Draw')
play()
    