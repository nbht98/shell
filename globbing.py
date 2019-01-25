import glob

#########################
# Function to process input to handle case input have glob or not
# Get the last element of list input
# Put to glob to generate
#########################


#################################
# Function to check if glob char appear
# Return True : If the input contain any globbing character
# Return False : If not
#################################
def check_globbing(glob_input):
    list_glob_char = ["*", "?", "["]
    for char in glob_input:
        if char in list_glob_char:
            return True
    return False


# function to replace all of cmdline list having * ? or [] to glob-form
# input: list of cmdline
# output: list which is replace all * ? [] to true form
def input_globbing(cmdline):
    check = True
    res = []
    for glob_input in cmdline:
        if check_globbing(glob_input):
            if '.' in glob_input and '*' in glob_input:
                lst = get_list(glob_input)
            else:
                lst = [glob_input]
            for i in lst:
                list_glob_input = glob.glob(i)
                for item in list_glob_input:
                    res.append(item)
                    check = False
            if check:
                res.append(glob_input)
        else:
            res.append(glob_input)
    return ' '.join(res)


# merge two lst into 1 lst by add lst1 with all element in lst2
# input: lst1 and lst2
# output: lst = lst1 + lst2
def get_arr(lst1, lst2):
    new = []
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    if type(lst1) is list:
        for i in lst1:
            if type(lst2) is list:
                for j in lst2:
                    new.append(i + '/' + j)
            else:
                new.append(i + '/' + lst2)
    else:
        if type(lst2) is list:
            for j in lst2:
                new.append(lst1 + '/' + j)
        else:
            new.append(lst1 + '/' + lst2)
    return new


# check if .* in string that is replaced with . .* and ..
# input: string include .*
# output: list of string replace .* into 3 . .* and ..
def get_input(string):
    new = []
    if '.?' in string:
        temp = string.find('*')
        string = string[0] + string[temp] + string[1:temp]
    pos = string.find(".*")
    new.append(string[:pos] + "." + string[pos+2:])
    if '?' in string:
        new[0] = new[0].replace('?','.')
    new.append(string[:pos] + ".." + string[pos+2:])
    new.append(string[:pos] + ".*" + string[pos+2:])
    return new


# get lst all case of globbing from string
# input: string need globbing
# output: string globbed
def get_list(string):
    temp = string.split("/")
    new = []
    for i in range(len(temp)):
        if "." in temp[i] and '*' in temp[i]:
            new = get_arr(new, get_input(temp[i]))
        else:
            new = get_arr(new, temp[i])
    return new
