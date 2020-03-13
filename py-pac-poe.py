state = {}

def play_game():
    init_game()
    get_win_count()
    while True:
        print_board()
        get_move()
        if result():
            print_board()
            print_result()
            set_score()
            if is_win_count():
                final_result()
                return
            else:
                reset_game()
        else:
            switch_turn()

def init_game():
    print(
        '\n-----------------------'
        "\n Let's play Py-Pac-Poe"
        '\n-----------------------'
    )
    state['win_count'] = 1
    state['score'] = { 'X': 0, 'O': 0, 'T': 0 }
    state['winner'] = None
    reset_game()

def reset_game():
    state['board'] = {
        'a1': ' ', 'b1': ' ', 'c1': ' ',
        'a2': ' ', 'b2': ' ', 'c2': ' ',
        'a3': ' ', 'b3': ' ', 'c3': ' '
    }
    state['turn'] = 'X'

def get_win_count():
    while True:
        try:
            count = int(input('\nHow many wins would you like to play to? (max: 5): '))
        except:
            print('Please enter a valid number...')
        else:
            if count in range(1, 5):
                state['win_count'] = count
                return
            else:
                print('Please enter a number between 1 and 5...')

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
            state['board'][move] = state['turn']
            return
        else:
            print('Bogus move! Try again...\n')

def switch_turn():
    state['turn'] = 'O' if state['turn'] == 'X' else 'X'
    
def result():
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
            return state['winner']
    state['winner'] = None if ' ' in state['board'].values() else 'T'
    return state['winner']

def print_result():
    if state['winner'] == 'T':
        print("It's a tie game!")
    else:
        print(f"Player {state['winner']} wins!")

def set_score():
    state['score'][state['winner']] += 1
    print(f"Score -- X: {state['score']['X']} | O: {state['score']['O']} | Ties: {state['score']['T']}")

def is_win_count():
    if state['score']['X'] < state['win_count'] and state['score']['O'] < state['win_count']:
        return False
    return True

def final_result():
    print(f"\nCongrats to Player {state['winner']} for winning {state['score'][state['winner']]} games!")

play_game()
