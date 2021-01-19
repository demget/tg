from tg import BasePackage


class Package(BasePackage):
    def emoji(self):
        return "📢"

    def name(self):
        return "Echo"

    def commands(self):
        return ["echo", "spam", "dice"]

    def echo(self, *v):
        return " ".join(v)

    def spam(self, n, *v):
        async def action(client, msg):
            for i in range(int(n)):
                if msg.reply_to_message:
                    await msg.reply_to_message.reply(" ".join(v))
                else:
                    await client.send_message(msg.chat.id, " ".join(v))
            await msg.delete()
            
        return action

    def dice(self, needed):
        async def action(client, msg):
            for _ in range(20):
                await msg.delete()
                msg = await client.send_dice(msg.chat.id)
                if msg.dice.value == int(needed):
                    break

        return action
