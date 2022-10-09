
from constants import PLYER_RULE


def check_one_hand(user_choice , system_choice):
    return PLYER_RULE[user_choice][system_choice]


def modify_scores(curent_result , curent_scores):
    if curent_result == 1 :
        curent_scores['user'] = curent_scores['user'] + 1
    elif curent_result == -1 :
        curent_scores['system'] = curent_scores['system'] + 1
    return curent_scores



def total_scores(curent_scores):
    if curent_scores['user'] == 3:
        curent_scores['total_user'] += 1 
        curent_scores['user'] = 0
        curent_scores['system'] = 0
        print ("#"*44 , '\tYou win\t' , "#"*44)

        print(f"\nTotal scores: {curent_scores['total_user']} , {curent_scores['total_system']}\n")

        print ("#"*115)

    elif curent_scores['system'] == 3 :
        curent_scores['total_system'] +=1
        curent_scores['user'] = 0
        curent_scores['system'] = 0
        print ("#"*44 , '\tYou Lost\t' , "#"*44)
        
        print(f"\nTotal scores: {curent_scores['total_user']} , {curent_scores['total_system']}\n")

        print ("#"*115)
    return curent_scores