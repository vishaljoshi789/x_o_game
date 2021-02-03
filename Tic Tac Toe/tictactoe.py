# Game board
# user input
# computer random input
# placing the x or o in board
# updating the board
# looping this above code till the all blocks fills
# checking for result
# restart for invalid input


game_board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
user_key = ''
comp_key = ''
switch = ''




def heading():
    print('------------------------ TIC TOK TOE --------------------------')
    print('             Code for the board are as follows                            ')
    print('                         1 | 2 | 3')
    print('                         4 | 5 | 6')
    print('                         7 | 8 | 9')
    print('---------------------------------------------------------------')
    print('                     Your board is-->>                                    ')


def board():
    print('                        ', game_board[0], '|', game_board[1], '|', game_board[2])
    print('                        ', game_board[3], '|', game_board[4], '|', game_board[5])
    print('                        ', game_board[6], '|', game_board[7], '|', game_board[8])


def key():
    choice = input("  Choose X or O : \n  ")
    global user_key, comp_key
    if choice == 'x' or choice == 'X':
        user_key = 'X'
        comp_key = 'O'
        print('  You chose', user_key)
    elif choice == 'o' or choice == 'O' or choice == 0:
        user_key = 'O'
        comp_key = 'X'
        print('  You chose', user_key)
    else:
        print("  You enter the invalid input. Please try again.")
        key()
def winners():
    if winner == user_key:

 	    print('  You Won!')


        
    elif winner == comp_key:
 	    print("  Computer Won!")
        
    else:
 	    if switch == 'user':
 		    print("  Its computer turn")
 		    comp()
 	    elif switch == 'comp':
 		    print("  Its your turn")
 		    user()

def win_check():
    global winner
    winner = ''
    if game_board[0] == game_board[1] == game_board[2] != '-':
        winner = game_board[0]
    elif game_board[3] == game_board[4] == game_board[5] != '-':
        winner = game_board[3]
    elif game_board[6] == game_board[7] == game_board[8] != '-':
        winner = game_board[6]
    elif game_board[0] == game_board[3] == game_board[6] != '-':
        winner = game_board[0]
    elif game_board[1] == game_board[4] == game_board[7] != '-':
        winner = game_board[1]
    elif game_board[2] == game_board[5] == game_board[8] != '-':
        winner = game_board[2]
    elif game_board[0] == game_board[4] == game_board[8] != '-':
        winner = game_board[0]
    elif game_board[2] == game_board[4] == game_board[6] != '-':
        winner = game_board[2]
    else:
    	pass
    winners()
def comp():
    if game_board[0] == user_key and game_board[1] == user_key and game_board[2] == '-':
        game_board.pop(2)
        game_board.insert(2, comp_key)
    elif game_board[0] == user_key and game_board[2] == user_key and game_board[1] == '-':
        game_board.pop(1)
        game_board.insert(1, comp_key)
    elif game_board[1] == user_key and game_board[2] == user_key and game_board[0] == '-':
        game_board.pop(0)
        game_board.insert(0, comp_key)
    elif game_board[3] == user_key and game_board[4] == user_key and game_board[5] == '-':
        game_board.pop(5)
        game_board.insert(5, comp_key)
    elif game_board[4] == user_key and game_board[5] == user_key and game_board[3] == '-':
        game_board.pop(3)
        game_board.insert(3, comp_key)
    elif game_board[3] == user_key and game_board[5] == user_key and game_board[4] == '-':
        game_board.pop(4)
        game_board.insert(4, comp_key)
    elif game_board[6] == user_key and game_board[7] == user_key and game_board[8] == '-':
        game_board.pop(8)
        game_board.insert(8, comp_key)
    elif game_board[7] == user_key and game_board[8] == user_key and game_board[6] == '-':
        game_board.pop(6)
        game_board.insert(6, comp_key)
    elif game_board[8] == user_key and game_board[6] == user_key and game_board[7] == '-':
        game_board.pop(7)
        game_board.insert(7, comp_key)
    elif game_board[0] == user_key and game_board[3] == user_key and game_board[6] == '-':
        game_board.pop(6)
        game_board.insert(6, comp_key)
    elif game_board[0] == user_key and game_board[6] == user_key and game_board[3] == '-':
        game_board.pop(3)
        game_board.insert(3, comp_key)
    elif game_board[3] == user_key and game_board[6] == user_key and game_board[0] == '-':
        game_board.pop(0)
        game_board.insert(0, comp_key)
    elif game_board[1] == user_key and game_board[4] == user_key and game_board[7] == '-':
        game_board.pop(7)
        game_board.insert(7, comp_key)
    elif game_board[1] == user_key and game_board[7] == user_key and game_board[4] == '-':
        game_board.pop(4)
        game_board.insert(4, comp_key)
    elif game_board[4] == user_key and game_board[7] == user_key and game_board[1] == '-':
        game_board.pop(1)
        game_board.insert(1, comp_key)
    elif game_board[2] == user_key and game_board[5] == user_key and game_board[8] == '-':
        game_board.pop(8)
        game_board.insert(8, comp_key)
    elif game_board[4] == user_key and game_board[7] == user_key and game_board[1] == '-':
        game_board.pop(1)
        game_board.insert(1, comp_key)
    elif game_board[1] == user_key and game_board[7] == user_key and game_board[4] == '-':
        game_board.pop(4)
        game_board.insert(4, comp_key)
    elif game_board[1] == user_key and game_board[4] == user_key and game_board[7] == '-':
        game_board.pop(7)
        game_board.insert(7, comp_key)
    elif game_board[0] == user_key and game_board[4] == user_key and game_board[8] == '-':
        game_board.pop(8)
        game_board.insert(8, comp_key)
    elif game_board[0] == user_key and game_board[8] == user_key and game_board[4] == '-':
        game_board.pop(4)
        game_board.insert(4, comp_key)
    elif game_board[4] == user_key and game_board[8] == user_key and game_board[0] == '-':
        game_board.pop(0)
        game_board.insert(0, comp_key) 
    elif game_board[4] == user_key and game_board[0] == user_key and game_board[8] == '-':
        game_board.pop(8)
        game_board.insert(8, comp_key)    
    elif game_board[2] == user_key and game_board[4] == user_key and game_board[6] == '-':
        game_board.pop(6)
        game_board.insert(6, comp_key)     
    elif game_board[2] == user_key and game_board[6] == user_key and game_board[4] == '-':
        game_board.pop(4)
        game_board.insert(4, comp_key)    
    elif game_board[4] == user_key and game_board[6] == user_key and game_board[2] == '-':
        game_board.pop(2)
        game_board.insert(2, comp_key) 
    else:
    	for i in range(len(game_board)):
    		if game_board[i] == '-':
    			game_board.pop(i)
    			game_board.insert(i, comp_key) 
    			break
    		else:
    			pass
    global switch
    switch = 'comp'
    board()
    win_check()

def user():
    try:
        code = input('  Enter the block number : \n  ')
        if code == 'vishal':
            global winner
            winner = user_key
            winners()
        else:
            codes = int(code)
            codes -= 1
            if game_board[codes] == '-':
                game_board.pop(codes)
                game_board.insert(codes, user_key)
                board()
                global switch
                switch = 'user'
                win_check()
            

            else:
                print('  The block is already occoupied')
                user()
        
    except Exception as e:
        print('You have typed the invalid input')
        user()


heading()
board()
key()
user()
