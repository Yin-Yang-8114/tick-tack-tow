bord = ["X","X","X","X","X","X","X","X","X"]
corrent_name = "gad"
corrent_user = "X"
game_running = True


def Column_check():
    if (corrent_user == bord[0] and corrent_user == bord[3] and corrent_user == bord[6]) or (corrent_user== bord[1] and corrent_user == bord[4] and corrent_user == bord[7]) or ( corrent_user == bord[2] and corrent_user == bord[5] and corrent_user == bord[8]):
        print(f"{corrent_name} win Column is {corrent_user} ,Congratulations!! ")
        return True
    else:
        return False

def Diagonal_check():
    if (corrent_user == bord[0] and corrent_user == bord[4] and corrent_user == bord[8]) or (corrent_user == bord[2] and corrent_user == bord[4] and corrent_user == bord[6]):
        print(f"{corrent_name} win Diagonal is {corrent_user} ,Congratulations!! ")
        return True
    else:
        return False
    
def main_check(corrent_name,corrent_user,game_running):
    if Column_check(corrent_name,corrent_user):
        game_running = False
        return game_running
    if Diagonal_check(corrent_name,corrent_user):
        game_running = False
        return game_running
    if check_row(corrent_name,corrent_user):
        game_running = False
        return game_running
    game_running = True
    return game_running
print(main_check(corrent_name,corrent_user,game_running))        

def check_row():
    if corrent_user == bord [0] and corrent_user == bord[1] and corrent_user == bord[2]:
        print( f" {corrent_name} he is the winner.")
        return True
    if corrent_user == bord[3] and corrent_user == bord[4] and corrent_user == bord [5]:
        print(f"{corrent_name} he is the winner.")
        return True
    if corrent_user == bord [6]and corrent_user == bord [7]and corrent_user == bord[8]:
        print(f"{corrent_name} he is the winner.")
        return True
    else:
        return False