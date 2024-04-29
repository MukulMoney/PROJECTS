import mysql.connector
from getpass4 import getpass
from tabulate import *
import random


def fall():
    mydb=mysql.connector.connect(host='localhost',
                                    user='root',
                                    database='Main',
                                    password='admin' ,
                                    auth_plugin='mysql_native_password'
                                    )
                                    
    
    return mydb
     
class Employee:
    @staticmethod
    def Employee():  
        db=fall()
        cur=db.cursor()

        print(''' -------------- Welcome Employee------------- ''')
        
        login = input("Enter Your LoginID:\n")
        password = getpass("Enter your Password:\n")

        sql = "select * from employee where empLoginId = '%s' and empPassword='%s'"
        values = (login, password)
        cur.execute(sql % values)
        while True:
                try:
                    row = cur.fetchmany(1)[0]
                    empPassword = row[1]
                    if password == empPassword:
                        print("Login authentication Successfully.\n\n")
                    empType = row[2]
                    
                    if empType == 'ADMIN':
                    
                        print(
                            "\n******************************* WELCOME ADMIN. ***********************************\n")

                        while True:
                            print("***************************************************************************************************************")
                            print("\n\n1.Customer Service.")
                            print("2.Employee Service.")
                            print("3.Game Service.")
                            print("4.EXIT\n\n")

                            c=input("Please Enter Your Choice :)\n")
                            if c==str(1):
                                while True:
                                    print('''------Welcome To Customer Service------
                                        \n Select The Service You Want To Use:
                                            1.Customer: View All
                                            2.Customer: Search - by Customer Name
                                            3.Customer: Search - by Customer Login Id
                                            4.Exit''')
                                    
                                    d=input("Please Enter Your Choice :)\n")

                                    if d==str(1):
                                        try:
                                            s="select * from customer"

                                            cur.execute(s)
                                            myre=cur.fetchall()

                                            print(tabulate(myre,headers=['custLoginId','custPassword','card_number','custName','custAge','custPhone','custEmail'],tablefmt='psql'))

                                            
                                            db.commit()

                                        except IndexError:
                                                print("Invalid,retry")
                                    
                                    elif d==str(2):
                                        try:
                                            y=input("Enter The Name Of The Customer You Want To Search:\n")

                                            s="select * from customer where custName LIKE %s"
                                            values=(y)

                                            cur.execute(s,('%' +y+ '%',))
                                            my=cur.fetchall()
                                            
                                            if my:
                                                print(tabulate(my,headers=['custLoginId','custPassword','card_number','custName','custAge','custPhone','custEmail'],tablefmt='psql'))
                                                
                                            else:
                                                    print("Invalid Employee Name")
                            
                                            db.commit()
                                        except IndexError:
                                                print("Invalid,retry")

                                    elif d==str(3):
                                        try:
                                            f=input("Please Enter The Login ID: \n")

                                            s="select * from customer where custLoginId='%s'"
                                            values=(f)

                                            cur.execute(s % values)

                                            my=cur.fetchall()
                                            
                                            if my:
                                                print(tabulate(my,headers=['custLoginId','custPassword','card_number','custName','custAge','custPhone','custEmail'],tablefmt='psql'))

                                            else:
                                                    print("Enter A Valid Login ID")
                                            
                                            db.commit()

                                        except IndexError:
                                                print("Invalid Employee LoginID,Retry.")

                                    elif d==str(4):
                                        print("Thank You For Using Customer Service ")

                                        break
                                    
                            
                            elif c==str(2):
                                while True:
                                    print('''------Welcome To The Employee Service------
                                        \n Select The Service You Want To Use:
                                            1.Employee: Add New (Admin or Expert)
                                            2.Employee: View All
                                            3.Employee: Search - by Employee Name
                                            4.Employee: Search - by Employee Login Id
                                            5.Employee: Search - by Employee Type
                                            6.Employee: Activate or Deactivate
                                            7.Employee: Change Password
                                            8.Exit''')
                                    
                                    d=input("Please Enter Your Choice :)\n")

                                    if d==str(1):
                                            
                                        try:
                                            print("Please Enter The Following Details")

                                            empid=input("Enter Employee's ID:\n")
                                            empp=input("Enter Employee's Password:\n")
                                            empt=input("Enter Employee's Type:\n")
                                            ename=input("Enter Employee's Name:\n")
                                            empphone=input("Enter employee's Phone Number:\n")
                                            empe=input("Enter Employee's Email:\n")

                                            s="insert into employee(empLoginId, empPassword, empType, empName, empPhone, empEmail)" "values('%s', '%s', '%s', '%s', '%s', '%s');"
                                            values=(empid,empp,empt,ename,empphone,empe) 

                                            cur.execute(s % values)
                                            print("\nEmployee added successfully.\n")
                                            db.commit()
                                            
                                        except IndexError:
                                                print("Invalid,Retry.")

                                    elif d==str(2):
                                            
                                        try:
                                            s="select * from employee"

                                            cur.execute(s)
                                            myre=cur.fetchall()

                                            print(tabulate(myre,headers=['empLoginId','empPassword','empType','empName','empPhone','empEmail','EmpStatus'],tablefmt='psql'))

                                            
                                            db.commit()

                                        except IndexError:
                                                print("Invalid,retry")

                                    elif d==str(3):
                                            
                                        try:
                                            y=input("Enter The Name Of The Employee You Want To Search:\n")

                                            s="select * from employee where empName LIKE %s"
                                            values=(y)

                                            cur.execute(s,('%' +y+ '%',))
                                            my=cur.fetchall()
                                            
                                            if my:
                                                print(tabulate(my,headers=['empLoginId','empPassword','empType','empName','empPhone','empEmail','EmpStatus'],tablefmt='psql'))
                                                
                                            else:
                                                    print("Invalid Employee Name")
                            
                                            db.commit()
                                        except IndexError:
                                                print("Invalid,retry")

                                    elif d==str(4):
                                            
                                        try:
                                            f=input("Please Enter The Login ID: \n")

                                            s="select * from employee where empLoginId='%s'"
                                            values=(f)

                                            cur.execute(s % values)

                                            my=cur.fetchall()
                                            
                                            if my:
                                                print(tabulate(my,headers=['empLoginId','empPassword','empType','empName','empPhone','empEmail','EmpStatus'],tablefmt='psql'))

                                            else:
                                                    print("Enter A Valid Login ID")
                                            
                                            db.commit()

                                        except IndexError:
                                                print("Invalid Employee LoginID,Retry.")

                                    elif d==str(5):
                                            
                                        try:
                                            i=input("Enter The Employee Type:\n")

                                            s="select * from employee where empType='%s'"
                                            values=(i)

                                            cur.execute(s % values)

                                            my=cur.fetchall()

                                            if my:
                                                print(tabulate(my,headers=['empLoginId','empPassword','empType','empName','empPhone','empEmail','EmpStatus'],tablefmt='psql'))

                                            else:
                                                    print("Enter a Valid Employee Type")
                                            
                                            db.commit()
                                        except:
                                                print("Invalid Employee Type,Retry.")
                                    

                                    elif d==str(6):
                                        try:
                                            Status = input("Enter the Status You Want:")
                                            LoginId = input("Enter LoginId of Employee :")

                                            sql = "update employee set empStatus='%s' where empLoginId='%s'"

                                            values = (Status, LoginId)
                                            complete_sql = sql % values
                                            print("complete_sql = ", complete_sql)
                                            cur.execute(complete_sql)
                                            if cur.rowcount == 1:
                                                print("Type updated successfully")
                                            else:
                                                print("Record update failed")
                                            
                                            db.commit()

                                        except IndexError:
                                            print("Invalid please try again")

                                    elif d==str(7):
                                            Password = input("Enter the new Password:")
                                            LoginId = input("Enter LoginId of Employee for Password update:")

                                            sql = "update employee set empPassword='%s' where empLoginId='%s'"

                                            values = (Password, LoginId)
                                            cur.execute(sql % values)

                                            db.commit()

                                            if cur.rowcount == 1:
                                                print("Password updated successfully")
                                            else:
                                                print("Record update failed")

                                    elif d==str(8):
                                            print("Thank You For Using Enployee Services")

                                            break

                                    else:
                                            print("Invalid Input") 

                            elif c==str(3):
                                    while True:
                                        print('''-------------Wlecome To Game Services-----------
                                            Select The Service You Want To Use:
                                                1.Add A Game
                                                2.Game: View All
                                                3.Game: Search by Game_Id
                                                4.Game: Search by Difficulty
                                                5.Game: Search by No_Of_Players
                                                6.Exit''') 

                                        g=input("Enter Your Choice :)\n")

                                        if g==str(1):
                                            
                                            a=input("Enter The Game ID")
                                            b=input("Enter The Name Of The Game")
                                            c=input("Enter The Difficulty Of The Game")
                                            d=input("Enter The No of Players Required")

                                            s="insert into game(game_id,game_name,difficulty,No_of_players)" "values('%s','%s','%s','%s')"
                                            values=(a,b,c,d)

                                            cur.execute(s % values)
                                            db.commit()
                                            my=cur.fetchall()

                                            print(tabulate(my,headers=['game_id','game_name','difficulty','No_of_players'],tablefmt='psql'))

                                        elif g==str(2):
                                            
                                            s="select * from game"

                                            cur.execute(s)
                                            my=cur.fetchall()

                                            print(tabulate(my,headers=['game_id','game_name','difficulty','No_of_players'],tablefmt='psql'))

                                        elif g==str(3):
                                            try:
                                                f=input("Enter The ID of The Game")

                                                s="select * form game where game_id='%s'"
                                                values=(f)

                                                cur.execute(s % f)
                                                my=cur.fetchall()

                                                print(tabulate(my,headers=['game_id','game_name','difficulty','No_of_players'],tablefmt='psql'))

                                            except IndexError:
                                                print("Please Enter A Valid Game ID")

                                        elif g==str(4):
                                            try:
                                                h=input("Enter The Difficulty 'Difficult','Medium','Easy'")

                                                s="select * from game where difficulty='%s'"
                                                values=(h)

                                                cur.execute(s % h)
                                                my=cur.fetchall()

                                                print(tabulate(my,headers=['game_id','game_name','difficulty','No_of_players'],tablefmt='psql'))
                                            
                                            except IndexError:
                                                print("Please Enter A Valid Difficulty")

                                        elif g==str(5):
                                            try:
                                                j=input("Enter The No of Players ('1_Player','2_Players')")

                                                s="select * from game where No_of_players='%s'"
                                                values=(j)

                                                cur.execute(s % j)
                                                my=cur.fetchall()

                                                print(tabulate(my,headers=['game_id','game_name','difficulty','No_of_players'],tablefmt='psql'))

                                            except IndexError:
                                                print("Enter Correct No Of Players")

                                        elif g==str(6):
                                            print("Thank You For Using Game Services :)")

                                            break
                                    
                            elif c==str(4):
                                    print("See You Again Employee :)")

                                    break
                            
                            else:
                                 print("Please Enter A Valid Choice")
                    else:
                                print("Login Authentication failed")
                                continue
                except IndexError:
                        print("Invalid User Name .Retry...")
                        break
                break

class customer:

        @staticmethod
        def login():
            db=fall()
            cur=db.cursor()
            while True:

                print('''----------------- This Is The Login Panel ----------------- \n
                        1.) SignUp 
                        2.) Login
                        3.) Exit ''')

                t=input("Please Enter Your Choice :)\n")

                if t==str(1):
                    try:
                        id=[]
                        print("Please Provide The Following Information")

                        while True:
    
                            a = input("Enter a Login ID of Format CUS-XXXX: ")

                            # Validate the format of the entered ID
                            if not a.startswith("CUS-") or not a[4:].isdigit() or len(a) != 8:
                                print("Invalid format. Please enter a valid ID in the format CUS-XXXX.")
                                continue  # Restart the loop to ask for a valid ID

                            # Check if the entered ID already exists in the list
                            if a in id:
                                print("This ID is already taken. Please choose another one.")
                            else:
                                # Add the new ID to the list of customer IDs
                                id.append(a)
                                print("Login ID successfully registered.")
                            
                            b=input("Enter A Password\n")

                            c=random.randint(10000,99999)
                            print(f"Your Generated Card Number is {c}")

                            d=input("Enter Your Name\n")

                            e=input("Enter Your Age\n")

                            f=input("Enter Your Phone Number\n")

                            g=input("Enter Your E-mail\n")

                            s="insert into customer(custLoginId,custPassword,card_number,custName,custAge,custPhone,custEmail)" "values('%s','%s','%s','%s','%s','%s','%s')"
                            values=(a,b,c,d,e,f,g)

                            cur.execute(s % values)

                            db.commit()

                            print("Congratulation You Are Signed UP")

                            break

                    except IndexError:
                        print("Invalid Please try Again")

                        
                
                elif t==str(2):
                    print("Please Enter Your LoginID And Password To be Logged IN")

                    login = input("Enter Your LoginID:\n")
                    password = getpass("Enter your Password:\n")

                    sql = "select * from customer where custLoginId = '%s' and custPassword='%s'"
                    values = (login, password)
                    cur.execute(sql % values)
                    while True:
                            try:
                                row =cur.fetchmany(1)[0]
                                custPassword = row[1]
                                if password == custPassword:
                                    print("Login authentication Successfully.\n")
                                    
                                    while True:

                                        print('''---------- Welcome Customer -------------
                                                Please Select The Compartment You Want To Visit
                                                
                                                1.) Customer's Compartment
                                                2.) Game Compartment
                                                3.) Exit''')
                                        
                                        p=input("Please Enter Your Choice :)")

                                        if p==str(1):
                                            while True:
                                                print(''' ------------- Welcome To Customer Compartment ----------
                                                    
                                                        Please Choose From The Following :
                                                        1.) View Your Profile
                                                        2.) Update Profile
                                                        3.) Change Password
                                                        4.) exit''')
                                                
                                                k=input("Please Enter Your Choice :)\n")

                                                if k==str(1):
                                                    try:
                                                        l=input("Enter Your Login ID \n")
                                                        m=getpass("Enter Your Password \n")
                                                        s="select * from customer where custLoginId='%s' and custPassword='%s'"
                                                        values=(l,m)

                                                        cur.execute(s % values)
                                                        my=cur.fetchall()

                                                        print(tabulate(my,headers=['custLoginId','custPassword','card_number','custName','custAge','custPhone','custEmail'],tablefmt='psql'))
                                                    except IndexError:
                                                        print("Invalid Please try Again")

                                                elif k==str(2):
                                                    try:
                                                        while True:
                                                            print('''You Can Update Following In Your Profile
                                                                    1.) Name
                                                                    2.) Age
                                                                    3.) Phone Number
                                                                    4.) E-Mail
                                                                    5.) Exit''')
                                                            
                                                            v=input("Enter Your Choice :)\n")

                                                            if v==str(1):
                                                                q=input("Enter The New Name \n")
                                                                r=input("Enter Your Login ID \n")

                                                                s="update customer set custName='%s' where custLoginId='%s'"
                                                                values=(q,r)

                                                                cur.execute(s % values)
                                                                my=cur.fetchall()

                                                                db.commit()

                                                                if cur.rowcount == 1:
                                                                    print("Name updated successfully")
                                                                else:
                                                                    print("Profile update failed")

                                                                

                                                            elif v==str(2):
                                                                q=input("Enter The New Age")
                                                                r=input("Enter Your Login ID")

                                                                s="update customer set custAge='%s' where custLoginId='%s'"
                                                                values=(q,r)

                                                                cur.execute(s % values)
                                                                my=cur.fetchall()

                                                                db.commit()

                                                                if cur.rowcount == 1:
                                                                    print("Age updated successfully")
                                                                else:
                                                                    print("Profile update failed")

                                                            elif v==str(3):
                                                                q=input("Enter The New Phone Number")
                                                                r=input("Enter Your Login ID")

                                                                s="update customer set custPhone='%s' where custLoginId='%s'"
                                                                values=(q,r)

                                                                cur.execute(s % values)
                                                                my=cur.fetchall()

                                                                db.commit()

                                                                if cur.rowcount == 1:
                                                                    print("Phone Number updated successfully")
                                                                else:
                                                                    print("Profile update failed")

                                                            elif v==str(4):
                                                                q=input("Enter The New E-Mail")
                                                                r=input("Enter Your Login ID")

                                                                s="update customer set custEmail='%s' where custLoginId='%s'"
                                                                values=(q,r)

                                                                cur.execute(s % values)
                                                                my=cur.fetchall()

                                                                db.commit()

                                                                if cur.rowcount == 1:
                                                                    print("E-Mail updated successfully")
                                                                else:
                                                                    print("Profile update failed")

                                                            elif v==str(5):
                                                                print("Thank You")
                                                                break
                                                            
                                                            else:
                                                                print("Invalid Response")

                                                    except IndexError:
                                                        print("Please Enter Valid Choice :(")


                                                elif k==str(3):
                                                    Password = getpass("Enter the new Password:")
                                                    LoginId = input("Enter Your LoginId for Password update:")

                                                    sql = "update customer set custPassword='%s' where custLoginId='%s'"

                                                    values = (Password, LoginId)
                                                    cur.execute(sql % values)

                                                    db.commit()

                                                    if cur.rowcount == 1:
                                                        print("Password updated successfully")
                                                    else:
                                                        print("Record update failed")

                                                elif k==str(4):
                                                    print("Thank You For Using Customer Compartment")
                                                    break
                                                
                                                else:
                                                    print("Invalid Choice :(")
                                                    

                                        
                                        elif p==str(2):
                                            game.gamee()

                                        elif p==str(3):
                                            break
                                        
                                        else:
                                            print("Please Enter A Valid Choice :(")

                                else:
                                    print("Login Authentication failed")
                                    break
                            except IndexError:
                                print("Invalid User Name .Retry...")
                                break
                        
                elif t==str(3):
                    break

                else:
                    print("Please Enter A Valid Choice :)")
            
class game:
    
    def viewgame(self):
         
        mydb=mysql.connector.connect(host='localhost',
                                     user='root',
                                     database='Main',
                                     password='admin')

        cur=mydb.cursor()
      
        s="select game_name from game"

        cur.execute(s)
        myresult=cur.fetchall()

        print(tabulate(myresult,headers=['Game_name'],tablefmt='psql'))  

        mydb.commit 
    

    def No(self):
        db=fall()

        cur=db.cursor()

        s="select game_name,No_of_players from game"

        cur.execute(s)
        myresult=cur.fetchall()

        print(tabulate(myresult,headers=['Game_Name','No_of_Players'],tablefmt='psql'))
        
        db.commit
     
    def difficulty(self):
            mydb=mysql.connector.connect(host='localhost',
                                     user='root',
                                     database='Main',
                                     password='admin')

            cur=mydb.cursor()

            s="select game_name,difficulty From game"

            cur.execute(s)
            myresult=cur.fetchall()

            print(tabulate(myresult,headers=['Game_Name','Difficulty'],tablefmt='psql'))

            mydb.commit


    def playgame(self):

        print('''-------Choose A Game To Play---------
                        1.) snake's And Ladder's
                        2.) Rock,Papper And Scissors
                        3.) Tic,Tak,Toe
                        4.) Guessing The Number''')
                    
        a=input("Enter Your Choice\n")

        if a==str(1):
                    import random

                    ladder={1:38,4:14,9:31,21:42,28:84,51:67,72:91,80:99}
                    snake={17:7,54:34,62:19,64:60,87:36,93:73,95:75,98:79}

                    pos1=0
                    pos2=0

                    def Move(pos):

                        dice=random.randint(1,6)
                        print(f"The Dice Is Thrown And The Number Is :{dice}")

                        pos= pos+dice
                                    
                        if pos in ladder:
                            print("Congratulations You Got A Ladder")

                            pos=ladder[pos]

                            print(f"position : {pos}")

                        elif pos in snake:
                            print("You Have Been Bitten By Snake")

                            pos=snake[pos]

                            print(f"Position : {pos}")

                        else:
                            print(f"Position : {pos}")

                        print("\n")

                        return (pos)



                    print("--------------------- Welcome To Snake's And Ladder's---------------------- ")
                    print("\n")

                    print("Press 1 To Play \n")
                    print("Press 2 To Exit \n")

                    a=(input("Enter Your Choice :\n"))

                    if a==str(1):
                        while True:
                            A=(input("Player 1 press [1]\n"))

                            if A==str(1):

                                pos1=Move(pos1)

                                if pos1>=100:
                                    print("Congratulations You win The Game ")

                                    break
                                                
                            else:
                                print("Invalid Number")
                                                
                            print("Computer's Turn")
                            B=random.randint(2,2)

                            if B==2:

                                pos2=Move(pos2)

                                if pos2>=100:
                                    print("Congratulations Computer Wins The Game ")

                                    break

                            else:
                                print("Invalid Number")

                    elif a==str(2):
                            print("Thank You Playing The Game.Have A Good Day")
                            exit(game.gamee())
                            

                    else:
                        print("Invalid Choice")


        elif a==str(2):
            import random

            def gamewin(comp,you):
                if(comp==you):
                    return(None)
                elif comp=="r":
                    if you=="p":
                        return True
                    elif you=="s":
                        return False
                elif comp=="p":
                    if you=="r":
                        return False
                    elif you=="s":
                        return True
                elif comp=="s":
                    if you=="r":
                        return True
                    elif you=="p":
                        return False   

            while(True):
                        
                print("Do you want to play the game (yes/no)")

                a=input("Enter Your Choice\n")

                if a=="yes":
                    print("Computer's Turn : Rock(r), Paper(p) , Scissors(s)?\n")
                    randNo = random.randint(1,3)
                    if(randNo==1):
                                comp = "r"
                    elif(randNo==2):
                                comp = "p"
                    elif(randNo==3):
                                comp="s"

                    you=input("Your Turn : Rock(r), Papper(p) , Scissors(s)?\n")
                                        
                    a=gamewin(comp,you)

                    print(f"computer chose\n{comp}")
                    print(f"you chose\n{you}")

                    if(a==None):
                        print("This Is a Tie")
                                    
                    elif(a==True):
                        print("Congratulations! You Won")
                                
                    elif(a==False):
                        print("Sorry! You Loose")
                            
                else:
                    print("Thank You For Playing")
                    exit(game.gamee())

        elif a==str(3):

            print('''Do You Want To Play The Game?
                  Press 1 To Play
                  Press 2 To Exit''')
            y=input("please Enter Your Choice")
            if y==str(1):
                import random
                from datetime import datetime
                def print_board(board):
                    print("\n    1   2   3 \n")
                    print("1   " + board[0][0] + " | " + board[0][1] + " | " + board[0][2])
                    print("   ---+---+---")
                    print("2   " + board[1][0] + " | " + board[1][1] + " | " + board[1][2])
                    print("   ---+---+---")
                    print("3   " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "\n")
                def check_row(board, row):
                    return (board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][0] != " ")
                def check_column(board, col):
                    return (board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[0][col] != " ")
                def check_diagonals(board):
                    return (board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != " ") or\
                            (board[2][0] == board[1][1] and board[1][1] == board[0][2] and board[2][0] != " ")
                def check_winner(board):
                    for i in range(3):
                        if check_row(board, i):
                            return True
                        if check_column(board, i):
                            return True
                    if check_diagonals(board):
                        return True
                    return False
                def is_board_full(board):
                    for item in board:
                        if " " in item:
                            return False
                    return True
                def play(board):
                    while True:
                        row = input("Enter row number: ")
                        while not row.isdigit() or int(row) < 1 or int(row) > 3:
                            row = input("Enter row number between 1-3: ")
                        row = int(row)
                        col = input("Enter column number: ")
                        while not col.isdigit() or int(col) < 1 or int(col) > 3:
                            col = input("Enter column number between 1-3: ")
                        col = int(col)
                        if board[row-1][col-1] != " ":
                            print("Pick an empty box!")
                        else:
                            return (row-1, col-1)
                def play_random(board):
                    possible_moves = []
                    for row in range(len(board)):
                        for col in range(len(board[0])):
                            if board[row][col] == " ":
                                possible_moves.append((row, col))
                    
                    return possible_moves[random.randrange(len(possible_moves))]
                def main():
                    print("\n== Tic Tac Toe ==")
                    # Create an empty board
                    board = [ 
                        [" ", " ", " "],
                        [" ", " ", " "],
                        [" ", " ", " "]
                    ]
                    # Create 2 players
                    players = ["X", "O"]
                    # Player X plays first
                    turn = 0
                    while not is_board_full(board):
                        print_board(board)
                        if turn == 0:
                            # User input
                            print("You play!")
                            row, col = play(board)
                            board[row][col] = players[turn]
                            
                        else:
                            # Compuuter plays
                            print("Computer plays!")
                            row, col = play_random(board)
                            board[row][col] = players[turn]
                        # Check if the player won
                        if check_winner(board):
                            print_board(board)
                            print("You won!" if turn == 0 else "Computer won!")
                            break
                        
                        # Select the next player
                        turn = 1 - turn
                    
                    else:
                        print_board(board)
                        print("It's a tie!")
                main()
            elif y==str(2):
                 print("Thank You For Playing The Game")
                 exit(game.gamee())

                    
        elif a==str(4):
                        
                        print("Do You Wawnt To play the game(Yes/No)")

                        v=input("Enter Your Choice :)\n")

                        if v=='yes':
                            import random
                            randnumber=random.randint(1,100)

                            userguess=None
                            Guesses=0
                            while(userguess != randnumber):
                                userguess=int(input("Enter Your Guess \n"))
                                Guesses+= 1
                                if userguess==randnumber:
                                    print("You Guessed It Right!!")
                                else:
                                    if userguess>randnumber:
                                        print("You Guessed It Wrong Try A Smaller Number")
                                    else:
                                        print("You Guessed It Wrong Try A Larger Number")

                            print(f"You Guessed the Number in {Guesses} Guesses")

                        elif v=='no':
                             print("Thank You For Playing :)")
                             exit(game.gamee())
                    

        else:
                        print("Please Enter A Valid Choice :) ")

    def Exitgame(self):

        print("Thank You For Visiting The Game Zone.Hope You Enjoyed.Please Visit Again")

    @staticmethod
    def gamee():
        while True:
            print('''------- Welcome To The Game's Zone Game Compartment 
                            Choose Your Option To Proceed : 
                                1.) For All View Options
                                2.) To Play The Games
                                3.) To Exit''')

            r=input("Please Enter Your Choice \n")

            if r==str(1):

                    while True:
                
                            print(''' Here Are All Your View Options : 
                                
                                    1.) View All the Games
                                    2.) View According To Number Of Players 
                                    3.) View Accoring The Difficulty Level
                                    4.) Exit''')
                            

                            c=input("Please Enter Your Choice :) \n")

                            if c==str(1):
                                
                                game.viewgame()

                            elif c==str(2):
                                
                                game.No()

                            elif c==str(3):
                                
                                game.difficulty()

                            elif c==str(4):
                                print("Thank You For Using View Options :) ")

                                break
                                
                            else:
                                print("Choose a Valid Option")

                            print('\n')
                            print('\n')

            elif r==str(2):
                game.playgame()

            elif r==str(3):
                print("Thank You For Visiting Game Compartment")
                break

            else:
                print("Please Enter A Valid Choice :) ")

            print('\n')
            print('\n')

cus=customer()
emp=Employee()
game=game()

while True:
    print(''' ---------------------- Welcome To The Game's Zone----------------------
        \nHere Are Some Options :
            1.) Go To Employee Options
            2.) Go To Customer Options
            3.) Exit''')

    z=input("Please Enter Your Choice :)\n")

    if z==str(1):
        Employee.Employee()

    elif z==str(2):
        while True:
            print('''------------------------- Welcome Customers----------------------
                1.) Login/SignUp
                2.) Exit''')
            c=input("Please Choose An Option :)\n")

            if c==str(1):
                customer.login()

            elif c==str(2):
                print("Thank you customer :)")

                break

    elif z==str(3):
        print("Thank You For Using The Game Zone,have A Great Day :)")
        exit()

    else:
        print("Please Enter A Valid Choice :)")
