
from core import check_one_hand, modify_scores, total_scores
from random import choice
from constants import CONTROL_OPTIONS, PLYER_RULE
from constants import PLYER_OPTIONS ,RESULT_BANNER

scores = { 'user' : 0, 'system': 0 , 'total_user' : 0 , 'total_system': 0 }
play = True

while play:
    user_input = input("Entekhab kon (r --> rock , p --> paper , s ---> scissors  e ----> exit): ")
    system_choice = choice(list(PLYER_OPTIONS.keys()))
    if user_input in PLYER_OPTIONS.keys():
        result = check_one_hand(user_input , system_choice)
        scores = modify_scores(result , scores)
        
        print ("entekhbe shoma {} va entekhabe system {}  natije in mosabeghe {} , \t Scores: {} - {} ".format(
            PLYER_OPTIONS[user_input],PLYER_OPTIONS[system_choice],
            RESULT_BANNER[result],scores['user'],scores['system']
        ))
        scores = total_scores(scores)
    elif user_input in CONTROL_OPTIONS.keys():
        play = False
        print ("Bye")
        
    else :
        print ("Invalid input , please try again")

