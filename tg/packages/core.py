import time
from tg import BasePackage
from tg import loader


class Package(BasePackage):
    def emoji(self):
        return "⚙️"

    def name(self):
        return "Core"

    def commands(self):
        return ["ping", "reload"]

    def ping(self):
        async def action(client, msg):
            t = time.time()
            await msg.edit(f"🏓 Pong!")
            t = time.time() - t
            await msg.edit(f"🏓 Pong! {int(t * 1000)}ms")

        return action

    def reload(self):
        async def action(_, msg):
            await msg.delete()
            
        loader.force_load()
        return action
