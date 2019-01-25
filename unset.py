import os


def unset(_input):
    if _input:
        for i in _input:
            if _input.index(i) != 0:
                if i in os.environ:
                    del os.environ[i]
