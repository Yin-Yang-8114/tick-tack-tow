from win_check import main_check
from config import sing_plyer_1,sing_plyer_2,user_1,user_2
print("welcome to tick tack tow")

corrent_user = sing_plyer_1
corrent_name = user_1

bord = ["","","","","","","","",""]
game_running = True
time_of_run = 0





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
            if corrent_user == sing_plyer_1:
                bord[choice] = corrent_user
                if  main_check(corrent_name, corrent_user,bord):
                    game_running = False
                else:
                    corrent_name = user_2
                    corrent_user = sing_plyer_2
                    time_of_run +=1
            else:
                bord[choice] = corrent_user
                if   main_check(corrent_name, corrent_user,bord):
                    game_running = False
                else:
                    corrent_user = sing_plyer_1
                    corrent_name = user_1
                    time_of_run += 1
            print(
                f"  {bord[0]} | {bord[1]} | {bord[2]}  \n-----------\n  {bord[3]} | {bord[4]} | {bord[5]}  \n-----------\n  {bord[6]} | {bord[7]} | {bord[8]}")