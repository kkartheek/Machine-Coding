
import Board
import user
from random import randint

def roll_die():
    return randint(1,6)

if __name__ == '__main__':
    board = []
    cnt =0
    board.append(Board.Cell(0))
    for i in range(1,101):
        board.append(Board.Cell(i))
    num = int(input("Enter the number of users"))
    users =  input("Enter the users")
    usr = users.split()
    if len(usr) != num:
        raise ValueError
    usrl = [user.User(usr[i]) for i in range(num)]

    snakec = int(input("Enter the number of snakes "))
    snakel = []
    for i in range(snakec):
        tmp = []
        tmp.append(int(input("enter start")))
        tmp.append(int(input("enter end")))
        snakel.append(tmp)
    for i,j in snakel:
        board[i].add_snake(i,j)



    ladderc = int(input("Enter the number of ladders"))
    ladderl = []
    for i in range(ladderc):
        tmp =[]
        tmp.append(int(input("enter start")))
        tmp.append(int(input("enter end")))
        ladderl.append(tmp)

    for i,j in ladderl:
        board[i].add_ladder(i,j)


    while cnt != num:
        for i in range(num):
            die_num = roll_die()
            usr_pos = usrl[i].user_get_pos()
            new_pos = die_num+usr_pos
            new_pos = new_pos if new_pos <= 100 else usr_pos
            jump = 0
            if board[new_pos].has_ladder():
                jump = board[new_pos].get_ladder()
                print(f"user {usrl[i].user_get_name()} climbing ladder to {jump} ")
            elif board[new_pos].has_snake():
                jump =board[new_pos].get_snake()

                print(f"user {usrl[i].user_get_name()} swallowed by snake to {jump} ")
            else :
                jump = new_pos
                if jump > 100:
                    jump = usr_pos
                print(f"user {usrl[i].user_get_name()} moved to {jump} ")
            if usrl[i].user_move(jump):
                cnt+=1

        print("Game has ended")

