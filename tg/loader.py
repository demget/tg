import os
import importlib
from tg import logger


packages = {}
commands = {}

def force_load():
    logger.info('Loading packages...')

    packages.clear()
    commands.clear()

    for file in os.listdir("tg/packages"):
        name, ext = os.path.splitext(file)
        if ext != ".py":
            continue
        
        try:
            lib = importlib.import_module(f".packages.{name}", package="tg")
            importlib.reload(lib)
            pkg = lib.__getattribute__("Package")()
            packages[pkg.name()] = pkg

            for cmd in pkg.commands():
                commands[cmd] = pkg.__getattribute__(cmd)
        except Exception as e:
            logger.error(e)


force_load()
