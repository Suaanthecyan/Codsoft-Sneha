#Rock, Paper, Scissor Game:

import random
l=["rock","paper","scissors"]

'''
rock vs paper: paper wins
rock vs scissors: rock wins
paper vs scissors: scissors win
'''
while True:
    ccount=0
    ucount=0
    uc=int(input('''
Game Start...
1 Yes           
2 NO | Exit

        '''))
    
    if uc==1:
        for a in range(1,4):
            userInput=int(input('''
1 Rock
2 Paper
3 Scissors                   
            
         '''))

            if userInput==1:
                uchoice="rock"
            elif userInput==2:
                uchoice="paper"
            elif userInput==3:
                uchoice="scissors" 
            # print(uchoice)

            Cchoice=random.choice(l)
            # print(Cchoice)

            if Cchoice==uchoice:
                print("Computer Choice:", Cchoice)
                print("Your Choice:",uchoice)
                print("It's a tie..")
                ucount=ucount+1
                ccount=ccount+1

            elif(uchoice=="rock" and Cchoice=="scissors") or (uchoice=="paper" and Cchoice=="rock") or (uchoice=="scissors"and Cchoice=="paper"):
                print("Computer Choice:", Cchoice)
                print("Your Choice:",uchoice)
                print("You Win!!!")
                ucount=ucount+1 
                #ucount+=1
        
            else:
                print("Computer Choice:", Cchoice)
                print("Your Choice:",uchoice)
                print("You Lose...")
                ccount=ccount+1

            print("")

            print("Computer Score:", ccount)
            print("Your Score:", ucount)

        if ucount==ccount:
            print("Your Score", ucount)
            print("Computer Score", ccount)
            print("Game Draw!")

        elif ucount>ccount:
            print("Your Score", ucount)
            print("Computer Score", ccount)
            print("You Won!!")

        else:
            print("Your Score", ucount)
            print("Computer Score", ccount)
            print("You Lost:( ")

        i=int(input('''
Play Again?
1 Yes
2 NO
        '''))

        if i==2:
            break

    else:
        break
