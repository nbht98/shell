import os


def printenv(_input):
    if len(_input) == 1:
        for i in os.environ:
            return(i + '=' + os.environ[i])
    else:
        for i in _input:
            if _input.index(i) != 0:
                if i in os.environ:
                    return(os.environ[i])
