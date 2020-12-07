
import os

def display_board(board):

    os.system('cls')

    # DISPLAYING BOARD

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def assign_markers(player,markers_list):

    # ASSIGNING POSITION TO THE PLAYER INPUTS
       
    position = 0
    while True:
        position = input(f"{player} CHOOSE A POSITION (1 - 9) :-\n")

        # CHECKING IF THE POSITION IS FILLED OR NOT AND CHECKING THE INPUT IS CORECT OR NOT
        check = full_board_check(markers_list,position)
        
        if check == True:
            if position == '1':
                markers_list[1] = player
                break

            elif position == '2':
                markers_list[2] = player
                break

            elif position == '3':
                markers_list[3] = player
                break

            elif position == '4':
                markers_list[4] = player
                break

            elif position == '5':
                markers_list[5] = player
                break

            elif position == '6':
                markers_list[6] = player
                break

            elif position == '7':
                markers_list[7] = player
                break

            elif position == '8':
                markers_list[8] = player
                break

            elif position == '9':
                markers_list[9] = player
                break
    
            else:
                print("WRONG INPUT")

        elif check == False:
            print("THIS POSITION IS ALREADY TAKEN")
            continue         

    # DISPLAYING BOARD AFTER POSITION IS ASSIGN        
    display_board(markers_list)  

def full_board_check(board,position):
    '''
    This function checks the position of the user is valid or not
    try and except handles the exceptions
    '''

    try:
        number = int(position)
        if board[number] == ' ':
            return True
        else:
            return False                                                    
    except:
        print("Invalid input")

def result_func(markers_list,player):
    
    # RESULTS DECLARATION

    
    # HORIZONTAL WIN RESULT
    if markers_list[7] == markers_list[8] == markers_list[9] == player:
        return "win"
    elif markers_list[4] == markers_list[5] == markers_list[6] == player:
        return "win"
    elif markers_list[1] == markers_list[2] == markers_list[3] == player:
        return "win"
    

    # VERTICAL WIN RESULT
    elif markers_list[7] == markers_list[4] == markers_list[1] == player:
        return "win"
    elif markers_list[8] == markers_list[5] == markers_list[2] == player:
        return "win"
    elif markers_list[9] == markers_list[6] == markers_list[3] == player:
        return "win"

    
    # CROSS WIN RESULT
    elif markers_list[7] == markers_list[5] == markers_list[3] == player:
        return "win"
    elif markers_list[9] == markers_list[5] == markers_list[1] == player:
        return "win"

    
    # TIE RESULT
    elif ' ' not in markers_list:
        return "tie"    

def game():

    '''
    This is the main game function that will run the player choices and other functions 
    that will help to play this game
    '''

    # BOARD DECLARATION
    board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    

    # PLAYER MARKER SELECTION
    result = ''
    player_marker = ''
    
    while player_marker != 'X' and player_marker != 'O':
        player_marker = input("Player 1 choose your marker 'X' or 'O' :-\n").upper()
        
    if player_marker == 'X':
        player_1 = 'X'
        player_2 = 'O'
        
    elif player_marker == 'O':
        player_1 = 'O'
        player_2 = 'X'

    print("Please refer keyboard numpad for positions")
    print("'1' will be the bottom left corner and '9' will be the top right corner")    

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('---+---+---')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


    # SELECTING MARKER POSITIONS AND RESULTS
    while result != "win" and result != "tie":

        # PLAYER 1 TURN

        # CALLING THE REQUIRED FUNCTIONS

        assign_markers(player_1,board)

        # CHECKING RESULTS AFTER EACH AND EVRY ROUND

        result = result_func(board,player_1)

        if result == "win":
            print("CONGRATULATIONS PLAYER 1! YOU HAVE WON")
            break

        elif result == "tie":
            print("THIS GAME IS TIED")
            break

        # PLAYER 2 TURN

        # CALLING THE REQUIRED FUNCTIONS
                
        assign_markers(player_2,board)

        # CHECKING RESULTS AFTER EACH AND EVRY ROUND

        result = result_func(board,player_2)
        
        if result == "win":
            print("CONGRATULATIONS PLAYER 2! YOU HAVE WON")
            break
        
        elif result == "tie":
            print("THIS GAME IS TIED")
            break 


if __name__ == "__main__":
    start = ''
    
    # STARTING THE GAME
    print("*****WELCOME TO TIC-TAC-TOE GAME DESIGNED BY MAYURESH KOLI*****\n")

    while True:
        print("DO YOU WANT TO PLAY THIS GAME ?")
        start = input("TO START THIS GAME PRESS 'S' OR TO QUIT THIS GAME PRESS 'Q' :-\n").upper() 

        # CALLING THE MAIN GAME FUNCTION
        if start == "S":
            game()
            print("\n")

        elif start == "Q":
            print("THANK YOU FOR PLAYING THIS GAME")
            break

        else:
            print("\nSORRY WRONG INPUT\n")

