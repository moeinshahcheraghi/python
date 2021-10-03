PLYER_OPTIONS = {'r' : 'sang' , 'p' : 'kaghaz' , 's':'gheychi'}
CONTROL_OPTIONS = {'e' : 'EXITE'}


PLYER_RULE = {

    'r' :{'r' : 0 , 'p': -1 , 's' : 1},
    's' :{'r' : -1 , 'p': 1 , 's' : 0},
    'p' :{'r' : 1 , 'p': 0 , 's' : -1} 
   
}

RESULT_BANNER = {

    1 : "You win",
    0 : "Draws",
    -1 : "You lost"
}