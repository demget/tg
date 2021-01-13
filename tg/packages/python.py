from tg import BasePackage


class Package(BasePackage):
    def emoji(self):
        return "🐍"

    def name(self):
        return "Python"

    def commands(self):
        return ["py"]

    def py(self, *args):
        pass
