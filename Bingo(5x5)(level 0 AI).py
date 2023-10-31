import random
P=input("Enter Player name : ")
myAI="DELTJ AI"
bingo1=[['  ' for p in range(5)]for q in range(5)]
bingo2=[['  ' for p in range(5)]for q in range(5)]
bingdic1=dict()
bingdic2=dict()

#
def displaybingo(bingo1,bingo2,P,myAI):
    bingo=[bingo1,bingo2]
    print("\n%s Grid : "%(P),end=' '*(25-len(P)))
    print("%s Grid : "%(myAI))
    for i in range(5):
        print("--------------------------       --------------------------")
        print("| ",end='')
        for j in range(2):
            for k in range(5):
                if(j==1 and k==0):
                    print('~   |',end=' ')
                if((len(bingo[j][i][k])) == 1 or bingo[j][i][k]=='X'):
                    print(bingo[j][i][k],end='  | ')
                else:
                    print(bingo[j][i][k],end=' | ')
            print(end='  ')
        print()
    print("--------------------------       --------------------------\n")
#
def placexincombobingo(row1,col1,row2,col2,combobingo1,combobingo2):
    combobingo1[row1][col1]='X'
    combobingo1[col1+5][row1]='X'
    if(row1==col1):combobingo1[10][row1]='X'
    if(row1+col1==4):combobingo1[11][row1]='X'
    combobingo2[row2][col2]='X'
    combobingo2[col2+5][row2]='X'
    if(row2==col2):combobingo2[10][row2]='X'
    if(row2+col2==4):combobingo2[11][row2]='X'
#
def numposition(bingdic1,bingdic2,num):
    row1=bingdic1[num][0]
    col1=bingdic1[num][1]
    del bingdic1[num]
    row2=bingdic2[num][0]
    col2=bingdic2[num][1]
    del bingdic2[num]
    return row1,col1,row2,col2
#
def placenumbers(bing,bingdic):
    numlist=[str(x) for x in range(1,26)]
    for i in range(5):
        for j in range(5):
            num=random.choice(numlist)
            numlist.remove(num)
            bing[i][j]=num
            bingdic[num]=[i,j]
#
def checkBINGO(combobing):
    if(combobing.count(['X','X','X','X','X'])>=5):
        return 1
    else:
        return 0
#
def checknum(bingdic1,num):
    while(num not in bingdic1.keys()):
            print("Invalid number!",end='')
            num=input("Enter other number : ")
    return num
#
def generateinputforAI(bingdic1,bingdic2):
    num=random.choice(list(bingdic1.keys()))
    return num
#####
placenumbers(bingo1,bingdic1)
placenumbers(bingo2,bingdic2)
combobingo1=[['  ' for p in range(5)]for q in range(12)]
combobingo2=[['  ' for p in range(5)]for q in range(12)]
print("Lets play!".center(26*2+7,'.'))
displaybingo(bingo1,bingo2,P,myAI)
for n in range(5**2):
    if(n%2==0):
        num=input("%s's chance--Enter number : "%P)
        num=checknum(bingdic1,num)
        row1,col1,row2,col2=numposition(bingdic1,bingdic2,num)
        bingo1[row1][col1]='X'
        bingo2[row2][col2]='X'
        placexincombobingo(row1,col1,row2,col2,combobingo1,combobingo2)
        displaybingo(bingo1,bingo2,P,myAI)
        #print(combobingo1)
        #print(combobingo2)
        if(checkBINGO(combobingo1)==1):
            print("Congratulations!%s has won the MATCH!"%P)
            break
        elif(checkBINGO(combobingo2)==1):
            print("%s has won the MATCH!Better Luck Next Time"%myAI)
            break
    else:
        num=generateinputforAI(bingdic1,bingdic2)
        print("AI choice is :",num)
        row1,col1,row2,col2=numposition(bingdic1,bingdic2,num)
        bingo1[row1][col1]='X'
        bingo2[row2][col2]='X'
        placexincombobingo(row1,col1,row2,col2,combobingo1,combobingo2)
        displaybingo(bingo1,bingo2,P,myAI)
        #print(combobingo1)
        #print(combobingo2)
        if(checkBINGO(combobingo2)==1):
            print("%s has won the MATCH!Better Luck Next Time"%myAI)
            break
        elif(checkBINGO(combobingo1)==1):
            print("Congratulations!%s has won the MATCH!"%P)
            break


