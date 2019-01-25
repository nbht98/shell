from export import export
import os


def cd(_input):
    if len(_input) == 1:
        if 'HOME' not in os.environ:
            print("intek-sh: cd: HOME not set")
        else:
            os.chdir(os.environ['HOME'])
            export(['export'] + ['PWD=' + os.getcwd()])
    else:
        os.chdir(_input[1])
        export(['export'] + ['PWD=' + os.getcwd()])
