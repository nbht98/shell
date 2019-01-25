import os
import re


# write command to history
# input: command and filename
# output: command written in filename
def write_file(string, filename):
    if os.path.exists(filename) is False:
        f = open(filename, 'w')
        f.close()
    with open(filename, 'a+') as f:
        f.seek(0)
        lines = f.readlines()
        check = True
        if lines:
            if string == lines[-1][:-1]:
                check = False
        if check:
            f.write(string + '\n')


# print history from history file
# input: filename
# output: print history from filename
def get_history(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        res = "%4d" % (i + 1) + "  " + lines[i][:-1]
        print(res)


# change ! into command line in history file
def get_exclamation(string, filename):
    with open(filename) as f:
        lines = f.readlines()
    if len(string) > 0:
        pos = -1
        pattern1 = re.compile('!-?\\d+')
        pattern2 = re.compile('!\\S+')
        lst_1 = pattern1.findall(string)
        lst_2 = pattern2.findall(string)
        if '!!' in string:
            string = string.replace("!!", lines[len(lines) - 1][:-1])
        if lst_1:
            for i in lst_1:
                if abs(int(string[1:])) <= len(lines):
                    if i[1] == '-':
                        string = string.replace(i, lines[len(lines)
                                                - int(string[2:])][:-1])
                    else:
                        string = string.replace(i, lines[int(string[1:])
                                                - 1][:-1])
        if lst_2:
            for i in lst_2:
                for j in reversed(range(len(lines))):
                    if i[1:] in lines[j]:
                        string = string.replace(i, lines[j][:-1])
        return string
