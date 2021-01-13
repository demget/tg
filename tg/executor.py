import re
import subprocess
from tg.loader import packages, commands


ERROR_MESSAGE = "Command not found"
re_shell = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def execute_command(name, args):
    if name not in commands:
        return ERROR_MESSAGE
    return commands[name](*args)
    

def execute_shell(exec):
    bash = subprocess.Popen(
        ["/bin/bash"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        shell=True
    )

    out, _ = bash.communicate(exec.encode())
    if not out:
        return ERROR_MESSAGE
    return re_shell.sub("", out.decode())
