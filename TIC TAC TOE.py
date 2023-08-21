def print_board(x,z):
    a = "X" if x[0] else 'O' if z[0] else 0
    b = "X" if x[1] else 'O' if z[1] else 1
    c = "X" if x[2] else 'O' if z[2] else 2
    d = "X" if x[3] else 'O' if z[3] else 3
    e = "X" if x[4] else 'O' if z[4] else 4
    f = "X" if x[5] else 'O' if z[5] else 5
    g = "X" if x[6] else 'O' if z[6] else 6
    h = "X" if x[7] else 'O' if z[7] else 7
    i = "X" if x[8] else 'O' if z[8] else 8
    print(f"{a} | {b} | {c}")
    print(f"__|___|__")
    print(f"{d} | {e} | {f}")
    print(f"__|___|__")
    print(f"{g} | {h} | {i}")
def sum(a,b,c):
    return a+b+c
def win(x,z):

    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for j in win:
        if sum(x[j[0]],x[j[1]],x[j[2]]) == 3:
            print("X won the match")
            return 1
        if sum(z[j[0]],z[j[1]],z[j[2]]) == 3:
            print(" O won the match")
            return 0
    return -1
if __name__== "__main__" :
    x=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    z=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn=1 #1 for x and 0 for 0
    print("welcome to tic tac toe")
    while True:
        print_board(x,z)
        if turn==1:
            print("X's chance")

            value=int(input("please enter a value: "))

            x[value]=1
        else:
            print("O's chance")

            value = int(input("please enter a value: "))

            z[value]=1
        cwin=win(x,z)
        if cwin !=-1:
            print("match over")
            break
        else:
            print("it's a draw")


        turn=1-turn


