from tg import BasePackage
from tg.executor import execute_command


class Package(BasePackage):
    def emoji(self):
        return "🔄"

    def name(self):
        return "Loop"

    def commands(self):
        return ["repeat"]

    def repeat(self, n, *v):
        async def action(client, msg):
            name, args = v[0][1:], v[1:]            
            for i in range(int(n)):
                res = execute_command(name, args)
                if callable(res):
                    await res(client, msg)
                else:
                    await client.send_message(msg.chat.id, res)

        return action
