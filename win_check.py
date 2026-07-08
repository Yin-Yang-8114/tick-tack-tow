from config import to_check_row,to_check_col,to_check_diagonal

def Column_check(corrent_name, corrent_user,bord):
    if (corrent_user == bord[0] and corrent_user == bord[3] and corrent_user == bord[6]) or (
            corrent_user == bord[1] and corrent_user == bord[4] and corrent_user == bord[7]) or (
            corrent_user == bord[2] and corrent_user == bord[5] and corrent_user == bord[8]):
        if to_check_col:
            print(f"player {corrent_name} with sign {corrent_user} WON  buy column ,Congratulations!! ")
        return True
    else:
        return False


def Diagonal_check(corrent_name, corrent_user,bord):
    if (corrent_user == bord[0] and corrent_user == bord[4] and corrent_user == bord[8]) or (
            corrent_user == bord[2] and corrent_user == bord[4] and corrent_user == bord[6]):
        if to_check_diagonal:
            print(f"player {corrent_name} with sign {corrent_user} WON  buy Diagonal ,Congratulations!! ")
        return True
    else:
        return False



def row_check(corrent_name, corrent_user,bord):
    if ((corrent_user == bord[0] and corrent_user == bord[1] and corrent_user == bord[2]) or (
            corrent_user == bord[3] and corrent_user == bord[4] and corrent_user == bord[5])
            or (corrent_user == bord[6] and corrent_user == bord[7] and corrent_user == bord[8])):
        if to_check_row:
            print(f"player {corrent_name} with sign {corrent_user} WON  buy row ,Congratulations!! ")
        return True
    else:
        return False


def main_check(corrent_name, corrent_user,bord):
    if Column_check(corrent_name, corrent_user,bord):
        return to_check_col
    if Diagonal_check(corrent_name, corrent_user,bord):
        return to_check_diagonal
    if row_check(corrent_name, corrent_user,bord):
        return to_check_row
    return False