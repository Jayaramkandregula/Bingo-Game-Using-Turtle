from turtle import *
import turtle
import random
import time

hideturtle()
title("BINGO BOARD")
setup(1350,680)
bgcolor("#FF006E")
speed(10000)
boxbgcolor="black";hidingboxescolor="light green";namecolor="black";greetingscolor="green"
outlinegridcolor="white";numcolor="white";dotcolor="blue";strikelinecolor="blue"

P=textinput("Player ","Name : ")
myAI="DELTJ AI"
bingo1=[['  ' for p in range(5)]for q in range(5)]
bingo2=[['  ' for p in range(5)]for q in range(5)]
bingdic1=dict()
bingdic2=dict()

#
def drawbingoboard():
    pensize(3);up();goto(-550,250);down();fillcolor(boxbgcolor);
    begin_fill();fd(500);right(90);fd(500);right(90);fd(500);right(90);fd(500);end_fill()
    up();goto(50,250);down();fillcolor(boxbgcolor);setheading(0)
    begin_fill();fd(500);right(90);fd(500);right(90);fd(500);right(90);fd(500);end_fill()
    pensize(6);pencolor(outlinegridcolor);up();goto(-550,250);down();setheading(0)
    x=100
    for i in range(6):fd(500);up();goto(-550,250-x);down();x=x+100
    up();goto(-550,250);down();setheading(270)
    y=100
    for i in range(6):fd(500);up();goto(-550+y,250);down();y=y+100
    setheading(0);up();goto(50,250);down()
    x=100
    for i in range(6):fd(500);up();goto(50,250-x);down();x=x+100
    up();goto(50,250);setheading(270);down()
    y=100
    for i in range(6):fd(500);up();goto(50+y,250);down();y=y+100
#    
def writenumbersgrid1(row,col,number):
    if(len(number)<2):up();goto(-520+(col*100),160-(row*100));down();write(number,font=('calibri',50,"bold"))
    else:up();goto(-530+(col*100),160-(row*100));down();write(number,font=('calibri',50,"bold"))
#
def writenumbersgrid2(row,col,number):
    if(len(number)<2):up();goto(80+(col*100),160-(row*100));down();write(number,font=('calibri',50,"bold"))
    else:up();goto(70+(col*100),160-(row*100));down();write(number,font=('calibri',50,"bold"))
#
#
def drawlinegrid1(index):
    pencolor(strikelinecolor);up();pensize(20)
    if(index<5):goto(-520,200-(index*100));down();setheading(0);fd(430)
    elif(index>4 and index<10):goto(-500+((index-5)*100),220);down();setheading(270);fd(430)
    elif(index==10):goto(-520,220);down();setheading(315);fd(610)
    elif(index==11):goto(-80,220);down();setheading(225);fd(610)
#
def drawlinegrid2(index):
    pencolor(strikelinecolor);up();pensize(20)
    if(index<5):goto(80,200-(index*100));down();setheading(0);fd(430)
    elif(index>4 and index<10):goto(100+((index-5)*100),220);down();setheading(270);fd(430)
    elif(index==10):goto(80,220);down();setheading(315);fd(610)
    elif(index==11):goto(520,220);down();setheading(225);fd(610)
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
def checkBINGO(combobingo1,combobingo2,combos1,combos2):
    for x in combobingo1[:]:
        if (x==['X','X','X','X','X']):
            drawlinegrid2(combobingo1.index(['X','X','X','X','X']))
            combobingo1[combobingo1.index(['X','X','X','X','X'])]='-'
            combos1=combos1+1
    for x in combobingo2[:]:
        if (x==['X','X','X','X','X']):
            drawlinegrid1(combobingo2.index(['X','X','X','X','X']))
            combobingo2[combobingo2.index(['X','X','X','X','X'])]='-'
            combos2=combos2+1
    return combos1,combos2
#
def checknum(bingdic1,num):
    while(num not in bingdic1.keys()):
        num=textinput("Invalid Number!","Enter valid number : ")
    return num
#
def generateinputforAI(bingdic2):
    num=random.choice(list(bingdic2.keys()))
    return num
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

####
placenumbers(bingo1,bingdic1)
placenumbers(bingo2,bingdic2)
combobingo1=[['  ' for p in range(5)]for q in range(12)]
combobingo2=[['  ' for p in range(5)]for q in range(12)]
drawbingoboard()
up();pencolor(namecolor);goto(-550,265);down();write("%s Grid:"%(myAI),font=('calibri',25,'bold'))
up();goto(50,265);down();write("%s Grid:"%(P),font=('calibri',25,'bold'))
s=turtle.Turtle();s.hideturtle();s.speed(1000);s.pencolor(numcolor);s.pensize(8);s.setheading(315);s.up();s.goto(-550,-250)
s.down();s.fillcolor(numcolor);s.begin_fill();s.circle(354,360,4);s.end_fill()
pencolor(numcolor)
for i in range(5):
    for j in range(5):
        writenumbersgrid1(i,j,(bingo2[i][j]))
for i in range(5):
    for j in range(5):
        writenumbersgrid2(i,j,(bingo1[i][j]))
s1=turtle.Turtle();s1.hideturtle();s1.speed(1000);s1.pencolor(hidingboxescolor);s1.setheading(315);s1.up();s1.goto(-535,165);s1.down();s1.fillcolor(hidingboxescolor);s1.begin_fill();s1.circle(50,360,4);s1.end_fill()
s2=turtle.Turtle();s2.hideturtle();s2.speed(1000);s2.pencolor(hidingboxescolor);s2.setheading(315);s2.up();s2.goto(-435,165);s2.down();s2.fillcolor(hidingboxescolor);s2.begin_fill();s2.circle(50,360,4);s2.end_fill()
s3=turtle.Turtle();s3.hideturtle();s3.speed(1000);s3.pencolor(hidingboxescolor);s3.setheading(315);s3.up();s3.goto(-335,165);s3.down();s3.fillcolor(hidingboxescolor);s3.begin_fill();s3.circle(50,360,4);s3.end_fill()
s4=turtle.Turtle();s4.hideturtle();s4.speed(1000);s4.pencolor(hidingboxescolor);s4.setheading(315);s4.up();s4.goto(-235,165);s4.down();s4.fillcolor(hidingboxescolor);s4.begin_fill();s4.circle(50,360,4);s4.end_fill()
s5=turtle.Turtle();s5.hideturtle();s5.speed(1000);s5.pencolor(hidingboxescolor);s5.setheading(315);s5.up();s5.goto(-135,165);s5.down();s5.fillcolor(hidingboxescolor);s5.begin_fill();s5.circle(50,360,4);s5.end_fill()
s6=turtle.Turtle();s6.hideturtle();s6.speed(1000);s6.pencolor(hidingboxescolor);s6.setheading(315);s6.up();s6.goto(-535,65);s6.down();s6.fillcolor(hidingboxescolor);s6.begin_fill();s6.circle(50,360,4);s6.end_fill()
s7=turtle.Turtle();s7.hideturtle();s7.speed(1000);s7.pencolor(hidingboxescolor);s7.setheading(315);s7.up();s7.goto(-435,65);s7.down();s7.fillcolor(hidingboxescolor);s7.begin_fill();s7.circle(50,360,4);s7.end_fill()
s8=turtle.Turtle();s8.hideturtle();s8.speed(1000);s8.pencolor(hidingboxescolor);s8.setheading(315);s8.up();s8.goto(-335,65);s8.down();s8.fillcolor(hidingboxescolor);s8.begin_fill();s8.circle(50,360,4);s8.end_fill()
s9=turtle.Turtle();s9.hideturtle();s9.speed(1000);s9.pencolor(hidingboxescolor);s9.setheading(315);s9.up();s9.goto(-235,65);s9.down();s9.fillcolor(hidingboxescolor);s9.begin_fill();s9.circle(50,360,4);s9.end_fill()
s10=turtle.Turtle();s10.hideturtle();s10.speed(1000);s10.pencolor(hidingboxescolor);s10.setheading(315);s10.up();s10.goto(-135,65);s10.down();s10.fillcolor(hidingboxescolor);s10.begin_fill();s10.circle(50,360,4);s10.end_fill()
s11=turtle.Turtle();s11.hideturtle();s11.speed(1000);s11.pencolor(hidingboxescolor);s11.setheading(315);s11.up();s11.goto(-535,-35);s11.down();s11.fillcolor(hidingboxescolor);s11.begin_fill();s11.circle(50,360,4);s11.end_fill()
s12=turtle.Turtle();s12.hideturtle();s12.speed(1000);s12.pencolor(hidingboxescolor);s12.setheading(315);s12.up();s12.goto(-435,-35);s12.down();s12.fillcolor(hidingboxescolor);s12.begin_fill();s12.circle(50,360,4);s12.end_fill()
s13=turtle.Turtle();s13.hideturtle();s13.speed(1000);s13.pencolor(hidingboxescolor);s13.setheading(315);s13.up();s13.goto(-335,-35);s13.down();s13.fillcolor(hidingboxescolor);s13.begin_fill();s13.circle(50,360,4);s13.end_fill()
s14=turtle.Turtle();s14.hideturtle();s14.speed(1000);s14.pencolor(hidingboxescolor);s14.setheading(315);s14.up();s14.goto(-235,-35);s14.down();s14.fillcolor(hidingboxescolor);s14.begin_fill();s14.circle(50,360,4);s14.end_fill()
s15=turtle.Turtle();s15.hideturtle();s15.speed(1000);s15.pencolor(hidingboxescolor);s15.setheading(315);s15.up();s15.goto(-135,-35);s15.down();s15.fillcolor(hidingboxescolor);s15.begin_fill();s15.circle(50,360,4);s15.end_fill()
s16=turtle.Turtle();s16.hideturtle();s16.speed(1000);s16.pencolor(hidingboxescolor);s16.setheading(315);s16.up();s16.goto(-535,-135);s16.down();s16.fillcolor(hidingboxescolor);s16.begin_fill();s16.circle(50,360,4);s16.end_fill()
s17=turtle.Turtle();s17.hideturtle();s17.speed(1000);s17.pencolor(hidingboxescolor);s17.setheading(315);s17.up();s17.goto(-435,-135);s17.down();s17.fillcolor(hidingboxescolor);s17.begin_fill();s17.circle(50,360,4);s17.end_fill()
s18=turtle.Turtle();s18.hideturtle();s18.speed(1000);s18.pencolor(hidingboxescolor);s18.setheading(315);s18.up();s18.goto(-335,-135);s18.down();s18.fillcolor(hidingboxescolor);s18.begin_fill();s18.circle(50,360,4);s18.end_fill()
s19=turtle.Turtle();s19.hideturtle();s19.speed(1000);s19.pencolor(hidingboxescolor);s19.setheading(315);s19.up();s19.goto(-235,-135);s19.down();s19.fillcolor(hidingboxescolor);s19.begin_fill();s19.circle(50,360,4);s19.end_fill()
s20=turtle.Turtle();s20.hideturtle();s20.speed(1000);s20.pencolor(hidingboxescolor);s20.setheading(315);s20.up();s20.goto(-135,-135);s20.down();s20.fillcolor(hidingboxescolor);s20.begin_fill();s20.circle(50,360,4);s20.end_fill()
s21=turtle.Turtle();s21.hideturtle();s21.speed(1000);s21.pencolor(hidingboxescolor);s21.setheading(315);s21.up();s21.goto(-535,-235);s21.down();s21.fillcolor(hidingboxescolor);s21.begin_fill();s21.circle(50,360,4);s21.end_fill()
s22=turtle.Turtle();s22.hideturtle();s22.speed(1000);s22.pencolor(hidingboxescolor);s22.setheading(315);s22.up();s22.goto(-435,-235);s22.down();s22.fillcolor(hidingboxescolor);s22.begin_fill();s22.circle(50,360,4);s22.end_fill()
s23=turtle.Turtle();s23.hideturtle();s23.speed(1000);s23.pencolor(hidingboxescolor);s23.setheading(315);s23.up();s23.goto(-335,-235);s23.down();s23.fillcolor(hidingboxescolor);s23.begin_fill();s23.circle(50,360,4);s23.end_fill()
s24=turtle.Turtle();s24.hideturtle();s24.speed(1000);s24.pencolor(hidingboxescolor);s24.setheading(315);s24.up();s24.goto(-235,-235);s24.down();s24.fillcolor(hidingboxescolor);s24.begin_fill();s24.circle(50,360,4);s24.end_fill()
s25=turtle.Turtle();s25.hideturtle();s25.speed(1000);s25.pencolor(hidingboxescolor);s25.setheading(315);s25.up();s25.goto(-135,-235);s25.down();s25.fillcolor('light green');s25.begin_fill();s25.circle(50,360,4);s25.end_fill()
s.clear()

def clearbox(row,col):
    if(row==0 and col==0):s1.clear()
    elif(row==0 and col==1):s2.clear()
    elif(row==0 and col==2):s3.clear()
    elif(row==0 and col==3):s4.clear()
    elif(row==0 and col==4):s5.clear()
    elif(row==1 and col==0):s6.clear()
    elif(row==1 and col==1):s7.clear()
    elif(row==1 and col==2):s8.clear()
    elif(row==1 and col==3):s9.clear()
    elif(row==1 and col==4):s10.clear()
    elif(row==2 and col==0):s11.clear()
    elif(row==2 and col==1):s12.clear()
    elif(row==2 and col==2):s13.clear()
    elif(row==2 and col==3):s14.clear()
    elif(row==2 and col==4):s15.clear()
    elif(row==3 and col==0):s16.clear()
    elif(row==3 and col==1):s17.clear()
    elif(row==3 and col==2):s18.clear()
    elif(row==3 and col==3):s19.clear()
    elif(row==3 and col==4):s20.clear()
    elif(row==4 and col==0):s21.clear()
    elif(row==4 and col==1):s22.clear()
    elif(row==4 and col==2):s23.clear()
    elif(row==4 and col==3):s24.clear()
    elif(row==4 and col==4):s25.clear()
def drawdot(g1row,g1col,g2row,g2col):
    up();pencolor(dotcolor);goto(-500+(g2col*100),200-(g2row*100));pensize(10);dot()
    up();pencolor(dotcolor);goto(100+(g1col*100),200-(g1row*100));pensize(10);dot()

numwrite=turtle.Turtle();numwrite.hideturtle();numwrite.speed(1000);numwrite.up();numwrite.goto(-550,-285);numwrite.down()
combos1,combos2=0,0
for n in range(5**2):
    if(n%2==0):
        num=textinput("%s's chance : "%(P),"Enter Number : ")
        num=checknum(bingdic1,num)
        row1,col1,row2,col2=numposition(bingdic1,bingdic2,num)
        N=turtle.Turtle();N.hideturtle();N.speed(1000);N.up()
        if(len(num)>1):N.goto(-37,-10);N.down();N.pencolor('#07AA93');N.write(num,font=('calibri',60,'bold'))
        elif(len(num)==1):N.goto(-20,-10);N.down();N.pencolor('#07AA93');N.write(num,font=('calibri',60,'bold'))
        bingo1[row1][col1]='X'
        bingo2[row2][col2]='X'
        drawdot(row1,col1,row2,col2)
        clearbox(row2,col2);time.sleep(2)
        placexincombobingo(row1,col1,row2,col2,combobingo1,combobingo2)
        #displaybingo(bingo1,bingo2,P,myAI)
        N.clear()
        numwrite.write('%s ,'%(num),font=('calibri',15,'bold'),move=True)
        combos1,combos2=checkBINGO(combobingo1,combobingo2,combos1,combos2)
        if(combos1>=5):
            up();pencolor(greetingscolor);goto(-550,-330);down();write("Congratulations %s!!You won the MATCH!"%P,font=('calibri',30,'bold'))
            break
        elif(combos2>=5):
            up();pencolor(greetingscolor);goto(-550,-330);down();write("%s has won the MATCH!Better Luck Next Time"%myAI,font=('calibri',30,'bold'))
            break
    else:
        num=generateinputforAI(bingdic2)
        row1,col1,row2,col2=numposition(bingdic1,bingdic2,num)
        N=turtle.Turtle();N.hideturtle();N.speed(1000);N.up()
        if(len(num)>1):N.goto(-37,-10);N.down();N.pencolor('#07AA93');N.write(num,font=('calibri',60,'bold'))
        elif(len(num)==1):N.goto(-20,-10);N.down();N.pencolor('#07AA93');N.write(num,font=('calibri',60,'bold'))
        bingo1[row1][col1]='X'
        bingo2[row2][col2]='X'
        drawdot(row1,col1,row2,col2)
        clearbox(row2,col2);time.sleep(2)
        placexincombobingo(row1,col1,row2,col2,combobingo1,combobingo2)
        #displaybingo(bingo1,bingo2,P,myAI)
        N.clear()
        numwrite.write('%s ,'%(num),font=('calibri',15,'bold'),move=True)
        combos1,combos2=checkBINGO(combobingo1,combobingo2,combos1,combos2)
        if(combos2>=5):
            up();pencolor(greetingscolor);goto(-550,-330);down();write("%s has won the MATCH!Better Luck Next Time"%myAI,font=('calibri',30,'bold'))
            break
        elif(combos1>=5):
            up();pencolor(greetingscolor);goto(-550,-330);down();write("Congratulations %s!!You won the MATCH!"%P,font=('calibri',30,'bold'))
            break

s1.clear();s2.clear();s3.clear(),s4.clear();s5.clear();s6.clear();s7.clear();s8.clear();s9.clear();s10.clear()
s11.clear();s12.clear();s13.clear(),s14.clear();s15.clear();s16.clear();s17.clear();s18.clear();s19.clear();s20.clear()
s21.clear();s22.clear();s23.clear(),s24.clear();s25.clear()
exitonclick()
