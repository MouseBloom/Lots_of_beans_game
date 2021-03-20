# many beans
beans = 16
def decision1(a):
    if beans == 16:
        return 3
    elif beans ==  12 or beans == 11 or beans == 10:
        return beans-9
    elif beans == 8 or beans == 7 or beans == 6:
        return beans-5
    elif beans == 4:
        return 3
    elif beans == 3:
        return 2
    elif beans == 2:
        return 1
def decision2(a):
    if beans == 15:
        return 2
    elif beans == 14:
        return 1
    elif beans == 13:
        return 2
    elif beans <= 12 and beans >= 10:
        return beans - 9
    elif beans == 9:
        return 1
    elif beans <=8 and beans >= 7:
        return beans-5
    elif beans == 6:
        return 1
    elif beans == 5:
        return 1
    elif beans <= 4 and beans >=2:
        return beans - 1
    elif beans == 1:
        return "YOU HAVE DEFEATED ME!!!"

print('Who goes first?\n1-COMPUTER\n2-YOU')
answer = input().strip()
while answer.isdigit() == False and int(answer) != 1 and int(answer) != 2:
    print('Write 1 or 2')
    answer = input().strip()
if answer == '1':
    print('Yoy play as second player, type your decisions')
    print("Amount of beans = 16")
    while beans > 0:
        b = decision1(beans)
        beans = beans-b
        print('1st player takes', b, 'beans\nbeans =', beans)
        turn= input('Make your choice ').strip()
        while turn.isdigit() == False:
            print('You can`t make this, try again')
            turn = input('Make your choice ').strip()
        while  int(turn)<1 or int(turn)>3 or int(turn)>beans:
            print('You can`t make this, try again')
            turn = input('Make your choice ').strip()
        beans = beans-int(turn)
        print('2st player takes', int(turn), 'beans\nbeans =', beans)
        if beans == 0:
            print('YOU LOSE, AHAHA!!')
if answer == '2':
    print('You play as first player, type your decisions')
    print("Amount of beans = 16")
    while beans > 0:
        turn = input('Make your choice ').strip()
        while turn.isdigit() == False:
            print('You can`t make this, try again')
            turn = input('Make your choice ').strip()
        while  int(turn)<1 or int(turn)>3 or int(turn)>beans:
            print('You can`t make this, try again')
            turn = input('Make your choice ').strip()
        beans = beans-int(turn)
        if beans == 1:
            print("there is only 1 bean")
            print(decision2(beans))
            exit()
        print('1st player takes', int(turn), 'beans\nbeans =', beans)
        b = decision2(beans)
        beans = beans - b
        print('2nd player takes', b, 'beans\nbeans =', beans)
        if beans == 1:
            print('YOU LOSE, AHAHA!!')
            exit()
