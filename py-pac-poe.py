import re

state = {}

def print_board():
    print('\n       A   B   C\n\n'
        f"   1   {state['board']['a1']} | {state['board']['b1']} | {state['board']['c1']}\n"
        '      -----------\n'
        f"   2   {state['board']['a2']} | {state['board']['b2']} | {state['board']['c2']}\n"
        '      -----------\n'
        f"   3   {state['board']['a3']} | {state['board']['b3']} | {state['board']['c3']}\n")

def init_game():
    print('\n----------------------\n'
        "Let's play Py-Pac-Poe!\n"
        '----------------------')
    
    state['board'] = {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' '
    }
    state['turn'] = 'X'
    state['winner'] = None
    
    print_board()
    get_move()

def get_move():
    move = ''
    while not re.match('[A-Ca-c][1-3]', move) or state['board'][move] != ' ':
        print('Bogus move! Try again...\n')
        move = input(f"Player {state['turn']}'s move (example B2): ").lower()

    state['board'][move] = state['turn']
    
    state['turn'] = 'O' if state['turn'] == 'X' else 'X'
    
    print_board()
    check_winner()

def check_winner():
    get_move()

init_game()
