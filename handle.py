import os
import subprocess
from history import write_file, get_history
from cd import cd
from printenv import printenv
from export import export
from unset import unset
from exit import exit_func


def run_file(_input, check):
    flag = False
    if './' in _input[0]:
        subprocess.check_call(_input[0])
    else:
        PATH = os.environ['PATH'].split(':')
        for item in PATH:
            if os.path.exists(item+'/'+_input[0]):
                if check:
                    subprocess.check_call([item+'/'+_input.pop(0)]+_input)
                    flag = True
                    break
                else:
                    return(subprocess.check_output([item+'/' +
                                                    _input.pop(0)] + _input))
        if not flag and check:
            print("intek-sh: " + _input[0] + ": command not found")
            return


def handle_cmd(inp, cmdline, cur, check):
    if '!' not in inp:
        write_file(inp, cur + '/' + 'history')
    if 'cd' in cmdline[0]:
        cd(cmdline)
    elif 'pwd' in cmdline[0]:
        print(os.getcwd())
    elif 'printenv' in cmdline[0]:
        res = printenv(cmdline)
        return res
    elif 'export' in cmdline[0]:
        export(cmdline)
    elif 'unset' in cmdline[0]:
        unset(cmdline)
    elif 'history' in cmdline[0]:
        get_history(cur + '/' + 'history')
    elif 'exit' in cmdline[0]:
        exit_func(cmdline)
    else:
        run_file(cmdline, check)



exception = {1: 'There are no further items produced by the iterator.',
             2: 'Stop the iteration.',
             3: 'Not currently used.',
             4: 'The result of an arithmetic ' +
                'operation is to large to be represented.',
             5: ': There is a zero division or module operation is zero.',
             6: 'An assert statement fails.',
             7: 'An attribute reference or assignment fails.',
             8: 'A buffer related operation cannot be performed.',
             9: 'The input() function hits an end-of-file' +
                'condition without reading any data.',
             10: 'Import statement' +
                 ' has troubles trying to load a module.',
             11: 'A sequence subscript is out of range.',
             12: 'Key is not found in the set of existing keys.',
             13: 'Operation runs out of memory but' +
                 ' the situation may still be rescued.',
             14: 'A local or global name is not found.',
             15: 'An operation block on an object' +
                 ' set for non-blocking operation.',
             16: 'An operation on a child process failed.',
             17: 'A base class for connection-related issues.',
             18: 'A file or directory already exists.',
             19: ": No such file or directory.",
             20: 'A system call is interrupted' +
                 ' by an incoming signal.',
             21: 'A file operation is requested on a directory',
             22: 'A directory operation is requested on' +
                 ' something which is not a directory.',
             23: ': Permission denied.',
             24: 'A system function timed' +
                 ' out at the system level.',
             25: 'An error is detected that does not' +
                 ' fall in any of the other categories.',
             26: 'The parser encounters a syntax error',
             27: 'There is a system error',
             28: 'An operation or function is applied' +
                 ' to an object of inappropriate type.',
             29: 'An operation or function receives an' +
                 ' argument that has the right type but' +
                 ' an inppropriate value.'}


def get_handle_error(inp, cmdline, cur, check, function):
    try:
        function(inp, cmdline, cur, check)
    except StopIteration:
        return 1
    except StopAsyncIteration:
        return 2
    except FloatingPointError:
        return 3
    except OverflowError:
        return 4
    except ZeroDivisionError:
        return 5
    except AssertionError:
        return 6
    except AttributeError:
        return 7
    except BufferError:
        return 8
    except EOFError:
        return 9
    except ImportError:
        return 10
    except IndexError:
        return 11
    except KeyError:
        return 12
    except MemoryError:
        return 13
    except NameError:
        return 14
    except BlockingIOError:
        return 15
    except ChildProcessError:
        return 16
    except ConnectionError:
        return 17
    except FileExistsError:
        return 18
    except FileNotFoundError:
        return 19
    except InterruptedError:
        return 20
    except IsADirectoryError:
        return 21
    except NotADirectoryError:
        return 22
    except PermissionError:
        return 23
    except TimeoutError:
        return 24
    except RuntimeError:
        return 25
    except SyntaxError:
        return 26
    except SystemError:
        return 27
    except TypeError:
        return 28
    except ValueError:
        return 29
    except Exception:
        return 30
    return 0


def print_error(name, cmdline, exitcode):
    if exitcode != 0:
        if exitcode == 19:
            print(name + cmdline[1] + exception[exitcode])
        elif exitcode == 23:
            print(name + cmdline[1] + exception[exitcode])
        else:
            print(name + exception[exitcode])
