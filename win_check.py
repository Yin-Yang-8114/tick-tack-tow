


def Column_check():
    if (corrent_user == bord[0] and corrent_user == bord[3] and corrent_user == bord[6]) or (corrent_user== bord[1] and corrent_user == bord[4] and corrent_user == bord[7]) or ( corrent_user == bord[2] and corrent_user == bord[5] and corrent_user == bord[8]):
        game_running = False
        return f"{corrent_name} win Column is {corrent_user} ,Congratulations!! "
    else:
        return True

def Diagonal_check():
    if (corrent_user == bord[0] and corrent_user == bord[4] and corrent_user == bord[8]) or (corrent_user == bord[2] and corrent_user == bord[4] and corrent_user == bord[6]):
        game_running = False
        return f"{corrent_name} win Diagonal is {corrent_user} ,Congratulations!! "
    else:
        return True
    
def main_check():
    pass    

def check_row():
    if corrent_user == bord [0] and corrent_user == bord[1] and corrent_user == bord[2]:
        return f" {corrent_name} he is the winner."
    if corrent_user == bord[3] and corrent_user == bord[4] and corrent_user == bord [5]:
        return f"{corrent_name} he is the winner."
    if corrent_user == bord [6]and corrent_user == bord [7]and corrent_user == bord[8]:
        return f"{corrent_name} he is the winner."
    else:
        return