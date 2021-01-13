import os
import re
from tg.loader import packages, commands


def execute_command(name, args):
    if name not in commands:
        return "Command not found"
    return commands[name](*args)
    

def execute_shell(exec):
    out = os.popen(exec).read()    
    out = re.sub(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])", "", out)
    return out
