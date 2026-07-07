print("welcome to tick tack tow")
user_1 = input("first player enter your username ")
user_2=input("second player enter your username ")


sing_1 = "X"
sing_2 = "O"
corrent_user = sing_1
corrent_name = user_1

bord = ["","","","","","","","",""]
game_running = True
time_of_run = 0

def Column_check(corrent_name, corrent_user):
    if (corrent_user == bord[0] and corrent_user == bord[3] and corrent_user == bord[6]) or (
            corrent_user == bord[1] and corrent_user == bord[4] and corrent_user == bord[7]) or (
            corrent_user == bord[2] and corrent_user == bord[5] and corrent_user == bord[8]):
        print(f"{corrent_name} win Column is {corrent_user} ,Congratulations!! ")
        return True
    else:
        return False


def Diagonal_check(corrent_name, corrent_user):
    if (corrent_user == bord[0] and corrent_user == bord[4] and corrent_user == bord[8]) or (
            corrent_user == bord[2] and corrent_user == bord[4] and corrent_user == bord[6]):
        print(f"{corrent_name} win Diagonal is {corrent_user} ,Congratulations!! ")
        return True
    else:
        return False


def check_row(corrent_name, corrent_user):
    if corrent_user == bord[0] and corrent_user == bord[1] and corrent_user == bord[2]:
        print(f" {corrent_name} he is the winner.")
        return True
    if corrent_user == bord[3] and corrent_user == bord[4] and corrent_user == bord[5]:
        print(f"{corrent_name} he is the winner.")
        return True
    if corrent_user == bord[6] and corrent_user == bord[7] and corrent_user == bord[8]:
        print(f"{corrent_name} he is the winner.")
        return True
    else:
        return False


def main_check(corrent_name, corrent_user, game_running):
    if Column_check(corrent_name, corrent_user):
        return True
    if Diagonal_check(corrent_name, corrent_user):
        return True
    if check_row(corrent_name, corrent_user):
        return True
    return False






while game_running:
    if time_of_run >= 9:
        game_running = False
        print("drow")
    else:
        choice = int(input(f'hi {corrent_name} please choose your please 0-8 '))
        if bord[choice] != "":
            print("this number is already taken")
        else:
            bord[choice] = corrent_user
            if corrent_user == sing_1:
                bord[choice] = corrent_user
                if  main_check(corrent_name, corrent_user, game_running):
                    game_running = False
                else:
                    corrent_name = user_2
                    corrent_user = sing_2
                    time_of_run +=1
            else:
                bord[choice] = corrent_user
                if   main_check(corrent_name, corrent_user, game_running):
                    game_running = False
                else:
                    corrent_user = sing_1
                    corrent_name = user_1
                    time_of_run += 1
            print(
                f"  {bord[0]} | {bord[1]} | {bord[2]}  \n-----------\n  {bord[3]} | {bord[4]} | {bord[5]}  \n-----------\n  {bord[6]} | {bord[7]} | {bord[8]}")