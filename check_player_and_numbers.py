def get_num():
    while True:

        try:
            choice=int(input("enter a num between 0-8"))
            if choice < 0 or choice > 8:
                print("out of range. please enter a number between 0-8")
                continue

            return choice

        except ValueError:
            print("error!, enter only a number")
print(get_num())

