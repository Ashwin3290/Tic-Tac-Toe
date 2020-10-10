#starting
import tttd 
board=[' ' for x in range (10)]
def insertletter(letter,pos):
    board[pos]=board[pos].replace(' ',letter)
def spaceisfree(pos):
    return board[pos]==' '
def printboard(board):
    print('                                                                                                    ''     |      |')
    print('                                                                                                    '''+board[1]+'    |  ' +board[2]+ '   | ' +board[3])
    print('                                                                                                    ''     |      |')
    print('                                                                                                    ''------------------')
    print('                                                                                                    ''     |      |')
    print('                                                                                                    '''+board[4]+'    |  ' +board[5]+ '   | ' +board[6])
    print('                                                                                                    ''     |      |')
    print('                                                                                                    ''------------------')
    print('                                                                                                    ''     |      |')
    print('                                                                                                    '''+board[7]+'    |  ' +board[8]+ '   | ' +board[9])
    print('                                                                                                    ''     |      |')
    
def iswinner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9]==le)or(bo[4]==le and bo[5]==le and bo[6]==le)or(bo[1]==le and bo[2]==le and bo[3]==le)or(bo[1]==le and bo[4]==le and bo[7]==le)or(bo[2]==le and bo[5]==le and bo[8]==le)or(bo[3]==le and bo[6]==le and bo[9]==le)or(bo[1]==le and bo[5]==le and bo[9]==le)or(bo[3]==le and bo[5]==le and bo[7]==le)
def playermove1():
    run=True
    while  run:
        move=input('Please select an position to place an  X ,(1-9)\n')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceisfree(move):
                    run=False
                    insertletter('X',move)
                else :
                    print('Sorry , this space is occupied')
            else :
                print ('Plese type a number within the range')
                    
        except:
            print('Please type number')
def playermove2():
    run=True
    while  run:
        move=input('Please select an position to place an  O ,(1-9)\n')
        try:
            move=int(move)
            if move>0 and move<10:
                if spaceisfree(move):
                    run=False
                    insertletter('O',move)
                else :
                    print('Sorry , this space is occupied')
            else :
                print ('Plese type a number within the range')
                    
        except:
            print('Please type number')

            
        
def compmove2():
    import random
    possiblemoves=[x for x, letter in enumerate(board) if  letter ==' ' and x !=0]
    move=0
    if len(possiblemoves)==9:
        move=random.choice(possiblemoves)
        return move
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy=board[ : ]
            boardcopy[i]=let
            if iswinner(boardcopy,let) :
                move=i
                return move
    cornersopen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move=selectrandom(cornersopen)
        return move
    if 5 in possiblemoves:
        move=5
        return move
    edgesopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move=selectrandom(cornersopen)
        return move
    return move

def compmove():
    possiblemoves=[x for x, letter in enumerate(board) if  letter ==' ' and x !=0]
    move=0
    for let in ['O','X']:
        for i in possiblemoves:
            boardcopy=board[ : ]
            boardcopy[i]=let
            if iswinner(boardcopy,let) :
                move=i
                return move
    cornersopen=[]
    for i in possiblemoves:
        if i in [1,3,7,9]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move=selectrandom(cornersopen)
        return move
    if 5 in possiblemoves:
        move=5
        return move
    edgesopen=[]
    for i in possiblemoves:
        if i in [2,4,6,8]:
            cornersopen.append(i)
    if len(cornersopen)>0:
        move=selectrandom(cornersopen)
        return move
    return move
    
                
def selectrandom(li):
    import random
    ln=len(li)
    r=random.randrange(0,ln)
    return li[r]
def isboardfull(board) :
    if board.count(' ')>1:
        return False
    else:
        return True
def main(p) :
    w=0
    l=0
    d=0

    print('Lets start')
    printboard(board)

    while not(isboardfull(board) ):


              if (iswinner(board,'X')) :
                  w+=1
                  print('Well  Done,',p,'  You Won!')
              if not(iswinner(board,'O')) :
                  playermove1()
                  printboard(board)
              else :
                  l+=1
                  print('Sorry,computer won')
                  
                  break
              if not(iswinner(board,'X')) :
                  move=compmove()
                  if move==0 :
                      d+=1
                      print('Tie game !')
                  else :
                      insertletter('O',move)
                      print('Computer placed an \'O\' at',move,':')
                      printboard(board)
              else :
                  print('Well  Done,',p,'  Won!')
                  break
    tttd.check(p,w,l,d)

    
    if isboardfull(board) :
        print('Well played')

def maincomputer() :
    w=0
    l=0
    d=0

    print('Lets start')
    printboard(board)

    while not(isboardfull(board) ):


              if (iswinner(board,'X')) :
                  w+=1
                  print('computer 1 wins')
              if not(iswinner(board,'O')) :
                 move=compmove2()
                 if move==0 :
                      d+=1
                      print('Tie game !')
                 else :
                      insertletter('X',move)
                      print('Computer placed an \'X\' at',move,':')
                      printboard(board)
              else :
                  print('computer one wins')
                  break
                
              if not(iswinner(board,'X')) :
                  move=compmove()
                  if move==0 :
                      d+=1
                      print('Tie game !')
                  else :
                      insertletter('O',move)
                      print('Computer placed an \'O\' at',move,':')
                      printboard(board)
              else :
                  print('Well  Done computer  Won!')
                  break

def main1(p1,p2):
    wa=0
    la=0
    da=0
    wb=0
    lb=0
    db=0
    
    print('Lets start')
    printboard(board)

    while not(isboardfull(board) ):
              if not(iswinner(board,'O')) :
                  playermove1()
                  printboard(board)
              else :
                  print('Sorry,',p2,'  won')
                  wb+=1
                  la+=1
                  break
              if not(iswinner(board,'X')) :
                  playermove2()
                  printboard(board)
              else :
                  print('Well  Done,',p1,'  Won!')
                  wa+=1
                  lb+=1
                  break
    tttd.check(p1,wa,la,da)
    tttd.check(p2,wb,lb,db)
    if isboardfull(board) :
        
        print('Tie Game!')
def again():
    print('Welcome to Tic Tac Toe!')
    print('Every block is labeled from 1-9')
    print('Do you want to play with a friend or with the computer')
    print('Enter f for friend or c for computer:')
    a=input()
    if a=='f' or a=='F':
        p1=str(input('Enter name of Player 1'))
        p2=str(input('Enter name of Player 2'))
        main1(p1,p2)
    elif a.lower()=='c':
        p=str(input('Enter your name'))
        main(p)
    elif a.lower()=='cc':
        maincomputer()
        
again()
print('database updated ')
print('do you want to delete your whole record?')
print("it can't be undone")
ch=input('Yes or No ')
if ch=='yes' :
    s=input("Enter name of player ")
    i=False
    while i==False:
        try:
            tttd.delete(s)
            i=True
        except:
            print('Player  name does not exist')
            i=False
print('\n\n')
print('Do you want to see database')
q=input('Yes or No ')
if q=='yes' :
    i=True
    while True:        
        try:
            s=input("Enter name of player ")
            tttd.show(s)
            tttd.graph(s)
            break
        except:
            print('Player  name does not exist')
            continue
quit() 
#Ashwin_Developer
