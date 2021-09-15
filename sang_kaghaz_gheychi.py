import random
computer_select_dic = { "sang": 0 , "kaghaz" : 1 , "gheychi" : 2}

user_score = 0

computer_score = 0
round = 5 
while round > 0 :
    computer_select= random.randint(0,2)
    user_select = input("\nsang , kaghaz , gheychi ?? \n")
    if computer_select == 0 and user_select == "kaghaz":
        print (f"shoma {user_score} va pc {computer_score}")
        user_score +=1
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])
    elif computer_select == 0 and user_select == "gheychi":
        print (f"shoma {user_score} va pc {computer_score}")
        computer_score +=1
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])
        
    elif computer_select == 1 and user_select == "gheychi":
        print (f"shoma {user_score} va pc {computer_score}")
        user_score +=1
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])
       
    elif computer_select == 1 and user_select == "sang":
        print (f"shoma {user_score} va pc {computer_score}")
        computer_score +=1
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])
        
    elif computer_select == 2 and user_select == "kaghaz":
        print (f"shoma {user_score} va pc {computer_score}")
        computer_score +=1
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])

    elif computer_select == 2 and user_select == "sagn":
        print (f"shoma {user_score} va pc {computer_score}")
        user_score +=1
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])
    else:
        print (f"shoma {user_score} va pc {computer_score}")
        print ("\nentekhabe shoma " , user_select , "entekhabe pc " , list(computer_select_dic.keys())[computer_select])
        print ("javab barabr")
        user_score +=1
        computer_score +=1 
        
    round -= 1
print (f"\nshoma {user_score} va pc {computer_score}")
if computer_score > user_score:
    print("\nto bakhti")
elif computer_score < user_score:
    print ("\nto bordi")
else:
    print ("\nmosavi shodin")
        
