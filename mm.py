# print('WELCOME TO TIC TAC TOE GAME ')
# print('IN THIS GAME YOU NEED TO CHOOSE NUMBER BETWEEN 1 TO 9 INCLUDING BOTH 1 AND 9')
dict={'7':' ','8':' ', '9':' ',
      '4':' ','5':' ','6':' ',
      '1':' ','2':' ','3':' '}

board_keys = []

for key in dict:
    board_keys.append(key)

      #now we have to define a function which generates tic tac toe box.
def box(game):
    print(game['7'] +'|'+game['8']  +'|'+game['9'])
    print('_|_|_')
    print(game['4']+'|'+game['5']+'|'+game['6'])
    print('_|_|_')
    print(game['1']+'|'+game['2']+'|'+game['3'])
    print(' | | ')

def tictactoe():
    turn='X'
    count=0
    #as we need to iterate 9 numbers we will need to provide range 10.
    #every time we will need to show box so we will iterate the box
    for i in range(10):
        box(dict)
        print(f'hey,{turn}choose a number' )
        choice=input(' ')
        if dict[choice]==' ':
            dict[choice]=turn
            count+=1
        else:
            print('sorry the place is already occupied,choose another number')
            continue
        #now we need to check if X or O wins the game.
        if count>=5:
            if dict['7']==dict['5']==dict==['3']!=' ':#checking diagonally
                box(dict)
                print(f'***** {turn}won the game.*****')
                break

            elif dict['7']==dict['8']==dict==['9']!=' ':#checking top across
                box(dict)
                print(f'**** {turn}won the game.****')
                break
        
            elif dict['4']==dict['5']==dict==['6']!=' ':#checking middle across
                box(dict)
                print(f'***** {turn}won the game.****')
                break

            elif dict['1']==dict['2']==dict==['3']!=' ':#checking lower across
                box(dict)
                print(f'**** {turn}won the game.*****')
                break

            elif dict['7']==dict['4']==dict==['1']!=' ':#checking first column
                box(dict)
                print(f'***** {turn}won the game.********')
                break

            elif dict['8']==dict['5']==dict==['2']!=' ':#checking middle column
                box(dict)
                print(f'**** {turn}won the game.****')
                break

            elif dict['9']==dict['6']==dict==['3']!=' ':#checking end right column
                box(dict)
                print(f'**** {turn}won the game.****')
                break

            elif dict['1']==dict['5']==dict==['9']!=' ':#checking diagonally
                box(dict)
                print(f'**** {turn}won the game.****')
                break
        if count==9:
            print(f'**** Nobody won the game.****')
            break
        
        if turn=='X':
            turn='O'
        else:
            turn='X'

    question=input('do you want to continue playing? y/n :  ').lower()
    if question=='y':
        # for key in board_keys:
        #         dict[key] = " "
        tictactoe()
if __name__ == "__main__":                           
    tictactoe()