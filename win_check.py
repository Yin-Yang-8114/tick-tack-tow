sing_1 = "X"
sing_2 = "O"
user_1 = "gad"
user_2 = "chaim"
bord = ["X","O","O"
        ,"X","X","X"
        ,"O","X","X"]

def Column_check():
    if (sing_1 == bord[0] and sing_1 == bord[3] and sing_1 == bord[6]) or (sing_1 == bord[1] and sing_1 == bord[4] and sing_1 == bord[7]) or ( sing_1== bord[2] and sing_1 == bord[5] and sing_1 == bord[8]):
        game_running = False
        return f"{user_1} win Column is {sing_1} ,Congratulations!! "
    elif (sing_2 == bord[0] and sing_2 == bord[3] and sing_2 == bord[6]) or (sing_2 == bord[1] and sing_2 == bord[4] and sing_2 == bord[7]) or ( sing_2== bord[2] and sing_2 == bord[5] and sing_2 == bord[8]):
        game_running = False
        return f"{user_2} win Column is {sing_2} ,Congratulations!! "
    else:
        return True
    
def Diagonal_check():
    if (sing_1 == bord[0] and sing_1 == bord[4] and sing_1 == bord[8]) or (sing_1 == bord[2] and sing_1 == bord[4] and sing_1 == bord[6]):
        game_running = False
        return f"{user_1} win Diagonal is {sing_1} ,Congratulations!! "
    elif (sing_2 == bord[0] and sing_2 == bord[4] and sing_2 == bord[8]) or (sing_2 == bord[2] and sing_2 == bord[4] and sing_2 == bord[6]):
        game_running = False
        return f"{user_2} win Diagonal is {sing_2} ,Congratulations!! "
    else:
        return True