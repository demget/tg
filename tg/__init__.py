from .logging import logger
from .package import BasePackage
from pyrogram.session import Session


HEADER = "<a href='https://github.com/demget/tg'>demget/tg</a>"
Session.notice_displayed = True


__all__ = (
    "HEADER",
    "logger",
    "BasePackage"
)