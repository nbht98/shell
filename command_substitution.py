import subprocess
from subprocess import PIPE
from handle import run_file


#########################
# check_substitution function
# Return true for substitution
#########################
def check_substitution(item):
    substitution_syntax_1 = ['$', '(', ')']
    substitution_syntax_2 = ['`', '`']
    check_list_1 = []
    check_list_2 = []
    for char in item:
        if char in substitution_syntax_1:
            check_list_1.append(char)
            if "".join(check_list_1) == "".join(substitution_syntax_1):
                return True
        if char in substitution_syntax_2:
            check_list_2.append(char)
            if "".join(check_list_2) == "".join(substitution_syntax_2):
                return True
    return False


#####################################
# get_child_command function
# this function will get the command inside $ char
# return command
####################################
def get_command(item):
    if '$' in item and '(' in item and ')':
        pos_1 = item.find('$')
        pos_2 = item.find('(')
        pos_3 = item.find(')')
        if pos_2 == pos_1 + 1 and pos_3 > pos_2:
            return item[pos_2 + 1:pos_3]
    if '`' in item:
        pos_f = item.find('`')
        if '`' in item[pos_f + 1:]:
            pos_s = item[pos_f + 1:].find('`')
            return item[pos_f + 1:pos_f + 1 + pos_s]


###########################
# execute_child_command function
# this function will using subprocess module
# execute the command and get result
###########################
def get_output_command(command):
    res = ''
    p = run_file(command.split(' '), False)
    if p is not None:
        result = p.decode('utf-8')
        result = result.split('\n')
        return ' '.join(result)[:-1]
    return ''


#########################
# Main Function of this module
# It will call all neccesery function on this module
# Input is a list []
#########################
def get_substitution(cmdline):
    is_substitution = check_substitution(cmdline)
    if is_substitution:
        command = get_command(cmdline)
        output = get_output_command(command)
        if cmdline.find('`') != -1:
            pos_f = cmdline.find('`')
        elif cmdline.find('$') != -1:
            pos_f = cmdline.find('`')
        pos_s = pos_f + len(command) + 1
        result = cmdline.replace(cmdline[pos_f:pos_s + 1], output)
        return result  # return the list likes list cmdline
    return cmdline


def change_substitution(string):
    while '`' in string:
        string = get_substitution(string)
    while '$(' in string:
        string = get_substitution(string)
    return string
