from tg import BasePackage


class Package(BasePackage):
    def emoji(self):
        return "📢"

    def name(self):
        return "Echo"

    def commands(self):
        return ["afk", "spam", "dice"]

    def echo(self, v):
        return f"{self.emoji()} {v}"

    def afk(self):
        pass

    def spam(self, n, *v):
        async def action(client, msg):
            for i in range(int(n)):
                await client.send_message(msg.chat.id, " ".join(v))
            await msg.delete()
            
        return action

    def dice(self):
        pass
