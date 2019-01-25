import os


def export(_input):
    if _input:
        for i in _input:
            if _input.index(i) != 0:
                if '=' in i:
                    temp = i.split('=')
                    os.environ[temp[0]] = temp[1]
                else:
                    os.environ[i] = ''
