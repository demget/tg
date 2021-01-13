from tg import BasePackage
from tg import loader


class Package(BasePackage):
    def emoji(self):
        return "⚙️"

    def name(self):
        return "Core"

    def commands(self):
        return ["ping", "machine", "reload"]

    def ping(self):
        return "🏓 Pong!"

    def machine(self):
        pass

    def reload(self):
        async def action(_, msg):
            await msg.delete()
            
        loader.force_load()
        return action
