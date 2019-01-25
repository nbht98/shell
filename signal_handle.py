import signal
##############################################
# Signal handler
##############################################


def get_sigint(signum, frame):
    raise KeyboardInterrupt


def get_sigquit(signum, frame):
    pass


def get_sigterm(signum, frame):
    pass


def signal_handle():
    signal.signal(signal.SIGINT, get_sigint)
    signal.signal(signal.SIGQUIT, get_sigquit)
    signal.signal(signal.SIGTERM, get_sigterm)
