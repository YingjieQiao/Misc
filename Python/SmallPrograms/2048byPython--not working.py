import curses
import collections
import random

letter_codes = [ord(ch) for ch in 'WASDNIwasdni']
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
actions_dict = dict(zip(letter_codes, actions * 2))

def get_user_action(keyboard):    
    char = "N"
    while char not in actions_dict:    
        char = keyboard.getch()
    return actions_dict[char]
   
def transpose(field):
    return [list(row) for row in zip(*field)]
   
def invert(field): #This is not to get an invert matrix. It returns a martix that is written in the reverse order.
    return [row[::-1] for row in field]
   
class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win = win
        self.score = 0
        self.highscore = 0
        self.reset()
       
    def reset(self):
        if self.score> self.hightscore:
            self.highscore = self.score
        self.score = 0
        self.field = [[0 for i in range(self.width)] for j in range(self.height)]
        self.spawn()
        self.spawn()
       
    def spawn(self):
        new_element = 4 if random.randrange(100) > 89 else 2
        (i,j) = random.choice([[(i,j) for i in range(self.width)] for j in range(self.height) if self.field[i][j] == 0])
        self.field[i][j] = new_element
        return new_element
                       
    def move(self,direction):
        def move_row_left(row):
            def squeeze(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in len(row) - len(new_row)]
                return new_row
               
            def merge(row):
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(row[i] * 2)
                        self.score = row[i] * 2
                        pair = False
                    else:
                        if i < len(row)-1 and row[i] == row[i+1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return squeeze(merge(squeeze(row)))
       
        #
        moves = {}
        moves['Left']  = lambda field:                              \
                [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                              \
                invert(moves['Left'](invert(field)))
        moves['Up']    = lambda field:                              \
                transpose(moves['Left'](transpose(field)))
        moves['Down']  = lambda field:                              \
                transpose(moves['Right'](transpose(field)))

        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False  
        #I don't understand this part at all. Fuck this tutorial.
       
        if direction in moves:
            if self.move_is_possible(direction):
                self.field = moves[direction](self.field)
                self.spawn()
                return True
            else:
                return False        
       
    def is_win(self):
        return any(any(i >= self.win_value for i in row) for row in self.field)
   
    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)
                   
    def draw(self,screen):
        help_string1 = '(W)Up (A)Left (S)Down (D)Right'
        help_string2 = '(N)Restart (I)Exit'
        gameover_string = 'GAMEOVER!'
        win_string = 'YOU WIN!'
        def cast(string):
            screen.addstr(string + '\n')
       
        def draw_separator():
            line = '+' + ('+------' * self.width + '+')[1::]
            separator = collections.defaultdict(lambda: line)
            if not hasattr(draw_separator, 'counter'):
                draw_separator = 0
            cast(separator[draw_separator.counter])
            draw_separator.counter += 1
               
        def draw_row(row):
            cast(''.join('|{: ^5} '.format(num) if num > 0 else '|      ' for num in row) + '|')
           
        screen.clear()
        cast('SCORE: ' + str(self.score))
        if self.highscore != 0:
            cast('HIGHSCORE: ' + str(self.highscore))
        for row in self.field:
            draw_separator()
            draw_row(row)
        draw_separator()
        if self.is_win():
            cast(win_string)
        else:
            if self.is_gameover():
                cast(gameover_string)
            else:
                cast(help_string1)
                cast(help_string2)      

    def move_is_possible(self, direction):
        def row_is_left_movable(row):
            def change(i): # true if there'll be change in i-th tile
                if row[i] == 0 and row[i + 1] != 0: # Move
                    return True
                if row[i] != 0 and row[i + 1] == row[i]: # Merge
                    return True
                return False
            return any(change(i) for i in range(len(row) - 1))

        check = {}
        check['Left']  = lambda field:                              \
                any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:                              \
                 check['Left'](invert(field))

        check['Up']    = lambda field:                              \
                check['Left'](transpose(field))

        check['Down']  = lambda field:                              \
                check['Right'](transpose(field))

        if direction in check:
            return check[direction](self.field)
        else:
            return False

def main(stdscr):
    def init():
        game_field.reset()
        return 'Game'
     
    def not_game(state):
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        responses = collections.defaultdict(lambda: state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[action]
       
    def game():
        game_field.draw(stdscr)
        action = get_user_action(stdscr)
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        if game_field.move(action): #move successful
            if game_field.is_win(stdscr):
                return 'Win'
            if game_field.is_gameover():
                return 'Gameover'
        return 'Game'
       
    state_actions = {
        'Init': init,
        'Win': lambda: not_game('Win'),
        'Gameover': lambda: not_game('Gameover'),
        'Game': game
    }
   
    curses.use_default_colors()
    game_field = GameField(win=2048)
   
    state = 'Init'
   
    while state != 'Exit':
        state = state_actions[state]()
       
curses.wrapper(main)
                

    
    
    
    