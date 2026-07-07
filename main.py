print("welcome to tick tack tow")
user_1 = input("first player enter your username ")
user_2=input("second player enter your username ")


sing_1 = "X"
sing_2 = "O"
corrent_user = sing_1
corrent_name = user_1

bord = ["","","","","","","","",""]

for i in range(9):
    choice = int(input(f'hi {corrent_name} please choose your please 0-8 '))
    if corrent_user == sing_1:
        bord[choice] = corrent_user
        corrent_name = user_2
        corrent_user = sing_2
    else:
        bord[choice] = corrent_user
        corrent_user = sing_1
        corrent_name = user_1


    print(
        f"  {bord[0]} | {bord[1]} | {bord[2]}  \n-----------\n  {bord[3]} | {bord[4]} | {bord[5]}  \n-----------\n  {bord[6]} | {bord[7]} | {bord[8]}")
