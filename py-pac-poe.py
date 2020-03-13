state = {}

def play_game():
    init_game()
    while not state['winner']:
        print_board()
        handle_move(get_move())
        handle_turn()
        check_winner()
    print_board()
    handle_winner()

def init_game():
    print(
        '\n----------------------'
        "\nLet's play Py-Pac-Poen"
        '\n----------------------'
    )
    
    state['board'] = {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' '
    }
    state['turn'] = 'X'
    state['winner'] = None

def print_board():
    print(
f"""
      A   B   C

  1   {state['board']['a1']} | {state['board']['b1']} | {state['board']['c1']}
     -----------
  2   {state['board']['a2']} | {state['board']['b2']} | {state['board']['c2']}
     -----------
  3   {state['board']['a3']} | {state['board']['b3']} | {state['board']['c3']}
"""
    )

def get_move():
    while True:
        move = input(f"Player {state['turn']}'s move (example C2): ").lower()
        if move in state['board'] and state['board'][move] == ' ':
            return move
        else:
            print('Bogus move! Try again...\n')
    
def handle_move(move):
    state['board'][move] = state['turn']

def handle_turn():
    state['turn'] = 'O' if state['turn'] == 'X' else 'X'

def check_winner():
    win_list = [
        ['a1', 'b1', 'c1'],
        ['a2', 'b2', 'c2'],
        ['a3', 'b3', 'c3'],
        ['a1', 'a2', 'a3'],
        ['b1', 'b2', 'b3'],
        ['c1', 'c2', 'c3'],
        ['a1', 'b2', 'c3'],
        ['a3', 'b2', 'c1']
    ]

    for pos in win_list:
        if (state['board'][pos[0]] != ' ' and 
                state['board'][pos[0]] == state['board'][pos[1]] == state['board'][pos[2]]):
            state['winner'] = state['board'][pos[0]]
            return
    state['winner'] = None if ' ' in state['board'].values() else 'T'

def handle_winner():
    if state['winner'] == 'T':
        print("It's a tie game!")
    else:
        print(f"Player {state['winner']} wins!")

play_game()
