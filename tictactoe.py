from IPython.display import clear_output 
board=['1','2','3','4','5','6','7','8','9']
p1_mark=''
pr_mark=''
pn=''

def rs_board(board):
    board=['1','2','3','4','5','6','7','8','9']
    return board

def ds_board(board):
    
    print(board[6]+'|'+board[7]+'|'+board[8])
    print('-----')
    print(board[3]+'|'+board[4]+'|'+board[5])
    print('-----')
    print(board[0]+'|'+board[1]+'|'+board[2])

def pl_ip():
    p1_mark=''
    while p1_mark!='X' and p1_mark!='O':
        p1_mark=input('\nEnter marker for player 1 (Either X or O) ').upper()
    if p1_mark=='X':
        p2_mark='O'
    else:
        p2_mark='X'
    print('\nMarker for player 1 is {} and for player 2 is {}'.format(p1_mark,p2_mark))
    return p1_mark,p2_mark

def main_lg(board,p1_mark,p2_mark):
    clear_output()
    i=0
    while i<7:
        if board[i]==board[i+1]==board[i+2]:
            if p1_mark==board[i]:
                print('\n***Player 1 Won***\n')
            else:
                print('\n***Player 2 Won***\n')
            return True
        i+=3
    i=0
    while i<3:
        if board[i]==board[i+3]==board[i+6]:
            if p1_mark==board[i]:
                print('\n***Player 1 Won***\n')
            else:
                print('\n***Player 2 Won***\n')
            return True
        i+=1
        
    if board[0]==board[4]==board[8]:
        if p1_mark==board[0]:
            print('\n***Player 1 Won***\n')
        else:
            print('\n***Player 2 Won***\n')
        return True    
            
    if board[2]==board[4]==board[6]:
        if p1_mark==board[2]:
            print('\n***Player 1 Won***\n')
        else:
            print('\n***Player 2 Won***\n')
        return True

    x=''
    i=0
    while i<9:
        if board[i]!='X'and board[i]!='O':
            x=True
            return False
        i+=1
    if x!=True:
        print('\n***Game is Tied***\n')
        return True  

def main_ip(board,p1_mark,p2_mark,pn):
    v=False
    while v==False:
        pos=int(input('\nPlease enter a number for the board position player {}: '.format(pn+1)))
        pos-=1
        if board[pos]!='X' and board[pos]!='O':
            if pn==0:
                board[pos]=p1_mark
            else:
                board[pos]=p2_mark
            v=True
            return board
        else:
            print('Invalid Position')


cont='Y'
while cont=='Y':
    board=rs_board(board)
    ds_board(board)
    p1_mark,p2_mark=pl_ip()
    c=False
    pn=0
    while c!=True:
        
        pn=pn%2
        board=main_ip(board,p1_mark,p2_mark,pn)
        pn+=1
        c=main_lg(board,p1_mark,p2_mark)
        ds_board(board)
    cont=input('\nDo you want to play again (Y/N) \n').upper()
