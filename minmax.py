import random

order = random.random()
first = True
if order >= 0.5:
    print('あなたは先攻です')
else:
    print('あなたは後攻です')
    first = False

class State:
    def __init__(self):
        self.state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    def user_change_state(self, cell_num):
        self.state[cell_num] = 'o'
    
    def pc_change_state(self,cell_num):
        self.state[cell_num] = '×'


state = State()

def display_state():
    for i in range(0, len(state.state)):
        if(i%3 == 2):
            print(state.state[i])
            print('-+-+-')
        else:
            print(state.state[i], end="|")

def check_clear(state, player):
    clear_state = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in range(0, len(clear_state)):
        if state[clear_state[i][0]] == state[clear_state[i][1]] == state[clear_state[i][2]]:
            print(player + 'の勝利！！')
            global clear
            clear = True

display_state()

clear = False
if first == True:
    while clear == False:
        print('マスの番号を入力してください')
        cell_num = int(input())
        while type(state.state[cell_num]) is not int:
            print('マスの番号を選び直してください')
            cell_num = int(input())
        state.user_change_state(cell_num)
        check_clear(state.state, 'user')
        display_state()
        if clear == False:
            print('相手のターン')
            cell_num = random.randint(0,8)
            while type(state.state[cell_num]) is not int:
                cell_num = random.randint(0,8)
            state.pc_change_state(cell_num)
            check_clear(state.state, 'pc')
            display_state()
else:
    while clear == False:
        print('相手のターン')
        cell_num = random.randint(0,8)
        while type(state.state[cell_num]) is not int:
            cell_num = random.randint(0,8)
        state.pc_change_state(cell_num)
        check_clear(state.state, 'pc')
        display_state()
        if clear == False:
            print('マスの番号を入力してください')
            cell_num = int(input())
            while type(state.state[cell_num]) is not int:
                print('マスの番号を選び直してください')
                cell_num = int(input())
            state.user_change_state(cell_num)
            check_clear(state.state, 'user')
            display_state()
        



