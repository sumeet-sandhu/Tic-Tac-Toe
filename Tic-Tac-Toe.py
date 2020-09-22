
from graphics import *

win = GraphWin('Tic-Tac-Toe', 500, 500, autoflush=False) # give title and dimensions
count=0
win.items=[]

def board():
    label = Text(Point(250 , 50), 'Tic-Tac-Toe')
    label.setTextColor('grey')
    label.setStyle('italic')
    label.setSize(20)
    label.draw(win)
    
    board_outline = Rectangle(Point(100,100), Point(400,400))# Draw rectangle
    board_outline.setFill('grey')
    board_outline.setOutline('cyan')
    board_outline.setWidth(3)
    board_outline.draw(win)

    board_partition_1 = Line(Point(200, 100), Point(200, 400)) # set endpoints
    board_partition_1.setOutline('cyan')
    board_partition_1.setWidth(3)
    board_partition_1.draw(win)

    board_partition_2 = Line(Point(300, 100), Point(300, 400)) # set endpoints
    board_partition_2.setOutline('cyan')
    board_partition_2.setWidth(3)
    board_partition_2.draw(win)

    board_partition_3 = Line(Point(100, 200), Point(400, 200)) # set endpoints
    board_partition_3.setOutline('cyan')
    board_partition_3.setWidth(3)
    board_partition_3.draw(win)

    board_partition_4 = Line(Point(100, 300), Point(400, 300)) # set endpoints
    board_partition_4.setOutline('cyan')
    board_partition_4.setWidth(3)
    board_partition_4.draw(win)

    restart_button = Rectangle(Point(100,450), Point(200,475))# Draw button
    restart_button.setFill('grey')
    restart_button.setOutline('cyan')
    restart_button.setWidth(1)
    restart_button.draw(win)

    restart = Text(Point(150,463), 'Restart')
    restart.setTextColor('cyan')
    restart.setStyle('bold')
    restart.setSize(10)
    restart.draw(win)

    exit_button = Rectangle(Point(300,450), Point(400,475))# Draw button
    exit_button.setFill('grey')
    exit_button.setOutline('cyan')
    exit_button.setWidth(1)
    exit_button.draw(win)

    exitt = Text(Point(350,463), 'Exit')
    exitt.setTextColor('cyan')
    exitt.setStyle('bold')
    exitt.setSize(10)
    exitt.draw(win)
    
    display_block_board()


def set_block_list():
    for i in range(9):
        tile = Text(Point(150+(i%3)*100, 150+(i//3)*100), i+1)
        win.items.append(tile)
        
def Guide() :
    message = Text(Point(250, 422), 'Click on in any of the nine tiles')
    message.setTextColor('grey')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)

def game_ended():
    message = Text(Point(250, 422), "It's a tie, Better luck next time")
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)
    after_a_game()

def X_won():
    message = Text(Point(250, 422), "Congratulations 'X' You won the game")
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)
    after_a_game()

def O_won():
    message = Text(Point(250, 422),  "Congratulations 'O' You won the game")
    message.setTextColor('black')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)
    after_a_game()

def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()
    board()
    

def display_block_board():
    for i in range(9):
        win.items[i].setTextColor('cyan')
        win.items[i].setStyle('bold')
        win.items[i].setSize(10)
        win.items[i].draw(win)

def check_win():
    if (win.items[0].getText()==win.items[1].getText() and win.items[1].getText()==win.items[2].getText()):
        if win.items[0].getText()== 'X' :
            X_won()
        elif win.items[0].getText()== 'O' :
            O_won()
        return False
    elif (win.items[3].getText()==win.items[4].getText() and win.items[4].getText()==win.items[5].getText()):
        if win.items[3].getText()== 'X' :
            X_won()
        elif win.items[3].getText()== 'O' :
            O_won()
        return False
    elif (win.items[6].getText()==win.items[7].getText() and win.items[7].getText()==win.items[8].getText()):
        if win.items[6].getText()== 'X' :
            X_won()
        elif win.items[6].getText()== 'O' :
            O_won()
        return False
    elif (win.items[0].getText()==win.items[3].getText() and win.items[3].getText()==win.items[6].getText()):
        if win.items[0].getText()== 'X' :
            X_won()
        elif win.items[0].getText()== 'O' :
            O_won()
        return False
    elif (win.items[1].getText()==win.items[4].getText() and win.items[4].getText()==win.items[7].getText()):
        if win.items[1].getText()== 'X' :
            X_won()
        elif win.items[1].getText()== 'O' :
            O_won()
        return False
    elif (win.items[2].getText()==win.items[5].getText() and win.items[5].getText()==win.items[8].getText()):
        if win.items[2].getText()== 'X' :
            X_won()
        elif win.items[2].getText()== 'O' :
            O_won()
        return False
    elif (win.items[0].getText()==win.items[4].getText() and win.items[4].getText()==win.items[8].getText()):
        if win.items[0].getText()== 'X' :
            X_won()
        elif win.items[0].getText()== 'O' :
            O_won()
        return False
    elif (win.items[2].getText()==win.items[4].getText() and win.items[4].getText()==win.items[6].getText()):
        if win.items[2].getText()== 'X' :
            X_won()
        elif win.items[2].getText()== 'O' :
            O_won()
        return False
    else :
        for i in range(9):
            if win.items[i].getText() not in ['X','O'] :
                return True
        game_ended()
        return False

def restart ():
    count=0
    for i in range(9):
        win.items[i].setText(str(i+1))
    clear(win)
    Guide()
    mouse_events_handling()

def invalid_choice():
    message = Text(Point(250, 422), "That's a invalid choice")
    message.setTextColor('red')
    message.setStyle('italic')
    message.setSize(10)
    message.draw(win)
    

def mouse_events_handling():
    while (check_win()):
        p1=win.getMouse()
        if ( (p1.getX()>100 and p1.getX()<400) and (p1.getY()>100 and p1.getY()<400)):
            X=int((p1.getX()-100)//100)
            Y=int((p1.getY()-100)//100)
            global count
            if not (win.items[Y*3+X].getText()=='X') and not (win.items[Y*3+X].getText()=='O') :
                if count%2==0 :
                    win.items[Y*3+X].setText('X')
                else :
                    win.items[Y*3+X].setText('O')
                count+=1
                clear(win)
            else :
                invalid_choice()
        elif ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
        elif ((p1.getX()>300 and p1.getX()<400) and (p1.getY()>450 and p1.getY()<475)) :
            win.close()
            raise SystemExit() 
        
def after_a_game():
    p1=win.getMouse()
    if ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
    elif ((p1.getX()>300 and p1.getX()<400) and (p1.getY()>450 and p1.getY()<475)) :
            win.close()
            raise SystemExit() 
    else :
        clear(win)
        message = Text(Point(250, 422),  "Click on 'Restart' to play again (or) Click on 'Exit' to exit")
        message.setTextColor('grey')
        message.setStyle('italic')
        message.setSize(10)
        message.draw(win)
        p1=win.getMouse()
        if ((p1.getX()>100 and p1.getX()<200) and (p1.getY()>450 and p1.getY()<475)) :
            restart ()
        elif ((p1.getX()>300 and p1.getX()<400) and (p1.getY()>450 and p1.getY()<475)) :
            win.close()
            raise SystemExit() 
        else :
            after_a_game()


set_block_list()
board()
Guide()
mouse_events_handling()