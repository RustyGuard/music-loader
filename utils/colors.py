class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def header(msg):
        return bcolors.HEADER + msg + bcolors.ENDC

    @staticmethod
    def okblue(msg):
        return bcolors.OKBLUE + msg + bcolors.ENDC

    @staticmethod
    def okgreen(msg):
        return bcolors.OKGREEN + msg + bcolors.ENDC

    @staticmethod
    def warning(msg):
        return bcolors.WARNING + msg + bcolors.ENDC

    @staticmethod
    def fail(msg):
        return bcolors.FAIL + msg + bcolors.ENDC
