import abc
from typing import List


class BasePackage:
    def emoji(self) -> str:
        return "📦"

    @abc.abstractproperty
    def name(self) -> str:
        raise NotImplementedError

    @abc.abstractproperty
    def commands(self) -> List[str]:
        raise NotImplementedError
