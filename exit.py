def exit_func(_input):
    if len(_input) == 1:
        print('exit')
        exit()
    elif _input[1].isdigit():
        print('exit')
        if int(_input[1]) < 0 or int(_input[1]) > 255:
            exit(255)
        else:
            exit(int(_input[1]))
    else:
        print('exit')
        print("intek-sh: exit:")
        exit(128)
