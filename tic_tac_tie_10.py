import random

def show_board ():
    print('\033[2m  A B C D E F G H I J \033[0m')
    for row in range(0, len(board)):
        print('\033[2m{}\033[0m'.format(str(row)), ' '.join(board[row])) 


def place_symbol(x, y, syb):
    zaynyata = False
    if board[x][y] == empty_symbol:
        board[x][y] = syb
    else:
        zaynyata = True
    return zaynyata


def win_check(syb):
    for i in range(0,10):
        for i_ in range(0,6):
            if board[i][i_] == syb and board[i][i_ + 1] == syb and board[i][i_ + 2] == syb and board[i][i_ + 3] == syb:               
                for w in range(0, 4):
                    board[i][i_ + w] = '\033[1m\033[31m{}\033[0m'.format(syb)
                show_board ()
                print('         \033[2m* * *\033[0m')
                print('\033[32m    CONGRATULATIONS!\033[00m')
                print('        ',syb, 'WON.')
                print('         \033[2m* * *\033[0m') 
                exit()
        for i_ in range(0,6):
            if board[i_][i] == syb and board[i_ + 1][i] == syb and board[i_ + 2][i] == syb and board[i_ + 3][i] == syb:               
                for w in range(0, 4):
                    board[i_ +w][i] = '\033[1m\033[31m{}\033[0m'.format(syb)
                show_board ()
                print('         \033[2m* * *\033[0m')
                print('\033[32m    CONGRATULATIONS!\033[00m')
                print('        ',syb, 'WON.')
                print('         \033[2m* * *\033[0m')  
                exit()  
    for i in range(0,7):
        for i_ in range(0,6):
            if board[i][i_] == syb and board[i+1][i_ + 1] == syb and board[i+2][i_ + 2] == syb and board[i+3][i_ + 3] == syb:               
                for w in range(0, 4):
                    board[i +w][i_ + w] = '\033[1m\033[31m{}\033[0m'.format(syb)
                show_board ()
                print('         \033[2m* * *\033[0m')
                print('\033[32m    CONGRATULATIONS!\033[00m')
                print('        ',syb, 'WON.')
                print('         \033[2m* * *\033[0m')  
                exit()
    for i in range(3,10):
        for i_ in range(0,6):
            if board[i][i_] == syb and board[i-1][i_ +1] == syb and board[i-2][i_ +2] == syb and board[i-3][i_ + 3] == syb:               
                for w in range(0, 4):
                    board[i -w][i_ + w] = '\033[1m\033[31m{}\033[0m'.format(syb)
                show_board ()
                print('         \033[2m* * *\033[0m')
                print('\033[32m    CONGRATULATIONS!\033[00m')
                print('        ',syb, 'WON.')
                print('         \033[2m* * *\033[0m') 
                exit()


def check_free_space ():
    stil_free = False
    for line in board:
        for cell in line:
            if cell == empty_symbol:
                stil_free = True
                break
    if not stil_free:
        print('     DRAW!!! 🤝')
        exit()


def cpu_turn ():
    rand_x = random.randint(0, 9)
    rand_y = random.randint(0, 9)
    return list(dict_letter.keys())[list(dict_letter.values()).index(rand_x)] + str(rand_y)
   

print('\033[2m\033[32m⁜\033[0m'*25)
print('\033[2m\033[32m⁜⁜⁜\033[0m\033[1m  XpEcTuKu-HoLuKu  \033[0m\033[2m\033[32m⁜⁜⁜\033[0m')
print('\033[2m\033[32m⁜\033[0m'*25)
print('\033[2m\033[32m***\033[0m\033[6m     GAME MODE     \033[0m\033[2m\033[32m***\033[0m')
print('\033[2m\033[32m*\033[0m'*25)
print('\033[2m\033[32m***\033[0m 1  PLAY vs PLAYER \033[2m\033[32m***\033[0m')
print('\033[2m\033[32m*\033[0m'*25)
print('\033[2m\033[32m***\033[0m 2  PLAY vs CPU    \033[2m\033[32m***\033[0m')
print('\033[2m\033[32m*\033[0m'*25)
print('\033[2m\033[32m***\033[0m Q  to QUIT GAME   \033[2m\033[32m***\033[0m')
print('\033[2m\033[32m*\033[0m'*25)
while True:
    game_mode = input('  ENTER YOUR CHOICE : ').upper()
    match game_mode:
        case '1' | '2':
            print('         \033[2m* * *\033[0m')
            print('\033[32m       GET READY!\033[0m')
            print('         \033[2m* * *\033[0m')
            break
        case 'Q':
            print('         \033[2m* * *\033[0m')
            print('\033[33m  YOU`VE LEFT THE GAME!\033[0m')
            print('         \033[2m* * *\033[0m')
            exit()
        case _:
            print('         \033[2m* * *\033[0m')
            print('\033[31m       INCORRECT!\033[0m')
            print('         \033[2m* * *\033[0m')
             

dict_letter = {'A': 0,
        'B': 1,
        'C': 2,
        'D': 3,
        'E': 4,
        'F': 5,
        'G': 6,
        'H': 7,
        'I': 8,
        'J': 9}

empty_symbol = '\033[2m\033[32m▢\033[00m'

board = [[empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol], 
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol], 
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol], 
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol],
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol],
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol],
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol],
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol],
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol],
     [empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol,empty_symbol]]

show_board ()
round = 0
while True:
    round += 1
    while True:
        print('\033[2mROUND {}\033[0m'.format(round), end = ' ')
        print('\033[2m{}\033[0m'.format('       X TURN'))
        turn = input(' INPUT YOUR MOVE: ').upper()
        print('        \033[2m* * *\033[0m')
        if turn == 'Q':
            print('\033[33mX PLAYER LEFT THE GAME!\033[0m')
            print('       GAME OVER')
            print('        \033[2m* * *\033[0m') 
            exit()
        try:
            if not place_symbol(int(turn[1]),dict_letter[turn[0]], 'X'):
                break
            else:
                print('\033[31m THIS SPACE IS TAKEN.\033[0m')
        except KeyError:
            print('\033[31m  INCORRECT LETTER!\033[0m')
        except IndexError:
            print('\033[31m  INCORRECT NUMBER!\033[0m')
        except ValueError:
            print('\033[31m   CELL NOT EXIST!\033[0m')
    
    show_board ()
    check_free_space ()
    win_check('X')
    while True:
        print('\033[2mROUND {}\033[0m'.format(round), end = ' ')
        print('\033[2m{}\033[0m'.format('       0 TURN'))
        if game_mode == '1':
            turn = input(' INPUT YOUR MOVE: ').upper()
            print('        \033[2m* * *\033[0m')
            if turn == 'Q':
                print('\033[33m0 PLAYER LEFT THE GAME!\033[0m')
                print('       GAME OVER')
                print('         \033[2m* * *\033[0m')  
                exit()
        else: 
            turn = cpu_turn()
            print('     CPU TURN:', turn)
            print('        \033[2m* * *\033[0m')
        try:
            if not place_symbol(int(turn[1]),dict_letter[turn[0]], 'O'):
                break
            else:
                print('\033[31m THIS SPACE IS TAKEN.\033[0m')
        except KeyError:
            print('\033[31m  INCORRECT LETTER!\033[0m')
        except IndexError:
            print('\033[31m  INCORRECT NUMBER!\033[0m')
        except ValueError:
            print('\033[31m   CELL NOT EXIST!\033[0m')   
    show_board ()
    check_free_space ()
    win_check('O')



