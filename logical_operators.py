from handle import get_handle_error, print_error, handle_cmd


########################
# Function to check if input is a logical command
# if command have logical operator: return True
# if commnad does not have logical operator: return False
########################
def check_logical(cmdline):
    logical_list = ["&&", "||"]
    for item in cmdline:
        if item in logical_list:
            return True
    return False


######################################################
# Function to process the command has logical operator
# Using a list to contain command and logical operator
# list = [[[cmd],'operator'], [[cmd2], 'operator'], [[last_cmd], '']]
# last cmd will be contained with '' to mask it the last command
# return the list when finish
######################################################
def process_condion_command(cmdline):
    logical_list = ["&&", "||"]
    cmd_n_operator = []
    cmd_queue = []
    cmd = []
    for item in cmdline:
        if item not in logical_list:
            # get command before logical operator
            cmd.append(item)
        if item in logical_list:
            # put command tho queue
            cmd_n_operator.append(cmd)
            # put this operator to queue
            cmd_n_operator.append(item)
            cmd_queue.append(cmd_n_operator)
            # reset list
            cmd = []
            cmd_n_operator = []
    # append last cmd to list and 1 signal to exit
    cmd_n_operator.append(cmd)
    cmd_n_operator.append('')
    cmd_queue.append(cmd_n_operator)
    return cmd_queue


##################################
# Function to loop command have logical operator
# Pop each command and execute it
# Get exit is returned and check with logical operator
##################################
def loop_command(inp, process, cur, check):
    # print(process)
    # Pop first command to execute
    cmd_part = process.pop(0)
    # print(cmd_part)
    cmd = cmd_part[0]
    # After execute command, take exit_code
    exit_code = get_handle_error(inp, cmd, cur, check, handle_cmd)
    # print(exit_code)
    # Get first logical operator
    logical_op = cmd_part[1]
    while process:
        # Get next command for wait to execute
        next_cmd_ops = process.pop(0)
        next_cmd = next_cmd_ops[0]
        if exit_code == 0:
            if logical_op == "&&":  # Execute next command and get next logical
                exit_code = get_handle_error(inp, next_cmd, cur,
                                             check, handle_cmd)
                logical_op = next_cmd_ops[1]
                # print("&&")
            if logical_op == '||':  # Get next logical and pass to next loop
                logical_op = next_cmd_ops[1]
                pass
                # print('||')
        if exit_code != 0:
            print_error('intek-sh: ', cmd, exit_code)
            if logical_op == "&&":  # Get next logical and pass to next loop
                logical_op = next_cmd_ops[1]
                pass
                # print("&&")
            if logical_op == '||':  # Execute next command and get next logical
                logical_op = next_cmd_ops[1]
                exit_code = get_handle_error(inp, next_cmd, cur,
                                             check, handle_cmd)
    return exit_code

#########################
# Main function of logical_operator module
#########################


def main_process(inp, cmdline, cur, check):
    check_logic = check_logical(cmdline)
    if check_logic:
        process = process_condion_command(cmdline)
        loop_command(inp, process, cur, check)
    else:
        return get_handle_error(inp, cmdline, cur, check, handle_cmd)
