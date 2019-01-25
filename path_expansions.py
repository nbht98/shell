import sys
import os


# check if string is true form for expansion
def check_string(string):
    for i in string:
        if i.isalnum() is False and i != '_':
            return False
    return True


# get tilde of one string
# input: string with ~ or ~+ or ~-
# output: string expanse ~, ~+, ~-
def get_tilde(string):
    if string:
        if '~' in string:
            if '=' not in string and '!' not in string:
                if len(string) > 1:
                    if string[1] == '+':
                        return parameter_expansion("$PWD" + string[2:])
                    if string[1] == '-':
                        return parameter_expansion("$OLDPWD" + string[2:])
                return os.path.expanduser(string)
            else:
                temp = string[string.find('=')+1:].split(':')
                res = string[:string.find('=')+1]
                if check_string(res):
                    for i in temp:
                        res_tilde = get_tilde(i)
                        if res_tilde is None:
                            res_tilde = i
                        if temp.index(i) != len(temp) - 1:
                            res = res + res_tilde + ':'
                        else:
                            res = res + res_tilde
                    return res
    return string


# expansion tilde of all string
# input: string with ~ or ~+ or ~-
# output: string expanse ~, ~+, ~-
def tilde_expansion(string):
    temp = string.split(' ')
    res = ''
    if temp:
        for i in range(0, len(temp)):
            res = res + get_tilde(temp[i])
            if i != len(temp) - 1:
                res = res + ' '
    return res


# split string into ${} and string
def split_string(str, lchar, rchar):
    res = []
    if str[0] == lchar:
        str_s = str.find(rchar)
        res.append('$' + str[:str_s+1])
        if str_s + 1 < len(str):
            res.append(str[str_s+1:])
    else:
        str_f = str.find(lchar)
        res.append('$' + str[:str_f])
        res.append(str[str_f:])
    return res


# expanse one string with $ or ${} form
# input: string with $ or ${}
# output: string which is expansed
def get_parameter(string):
    temp = string.split('$')
    res = []
    new = ''
    if temp:
        for i in range(0, len(temp)):
            if i == 0 and temp[i] != '':
                res.append(temp[i])
            elif i > 0:
                if '(' and ')' in temp[i]:
                    res = res + split_string(temp[i], '(', ')')
                elif '{' and '}' in temp[i]:
                    res = res + split_string(temp[i], '{', '}')
                else:
                    res.append('$' + temp[i])
    if res:
        for i in res:
            if '$' in i[0] and '(' not in i:
                temp1 = os.path.expandvars(i)
                if '$' not in temp1:
                    new = new + temp1
            else:
                new = new + i
    return new


# expanse all of the string into parameter
# input: string with multiple $ or ${}
# output: string which is expansed
def parameter_expansion(string):
    temp = string.split(' ')
    res = ''
    if temp:
        for i in range(0, len(temp)):
            if '=' in temp[i]:
                res = res + get_parameter(temp[i][:temp[i].find('=')])
                res = res + get_parameter(temp[i][temp[i].find('='):])
            else:
                res = res + get_parameter(temp[i])
            if i != len(temp) - 1:
                res = res + ' '
    return res


# combine parameter and tilde expansion
def expansion(string):
    res = parameter_expansion(string)
    return tilde_expansion(res)
