#!/usr/bin/env python3
import os
import readline
from history import write_file, get_history, get_exclamation
from handle import get_handle_error
from path_expansions import expansion
from globbing import input_globbing
from logical_operators import main_process
from command_substitution import change_substitution
from signal_handle import signal_handle


exit_code = 0


def inputlst(_input, cur):
    global exit_code
    res = []
    _input = _input.replace("$?", str(exit_code))
    exclam_temp = get_exclamation(_input, cur + '/' + 'history')
    sub_temp = change_substitution(exclam_temp)
    temp = sub_temp.split(' ')
    for i in temp:
        i = i.lstrip(' ')
        i = i.rstrip(' ')
        if i != '':
            # res.append(i)
            res.append(expansion(i))
    res = input_globbing(res)
    res = change_substitution(res)
    return res.split(' ')


def main():
    check = True
    global exit_code
    cur = os.getcwd()
    signal_handle()
    try:
        while check:
            readline.parse_and_bind("tab: complete")
            try:
                inp = input('intek-sh$ ')
            except EOFError:
                return
            if inp.strip(' ') == '':
                inp = input('intek-sh$ ')
            else:
                exit_code = get_handle_error(inp,
                                             inputlst(inp, cur),
                                             cur, True, main_process)
    except KeyboardInterrupt:
        print("^C")
        exit_code = 130
        main()
    except Exception:
        main()


if __name__ == '__main__':
    main()
