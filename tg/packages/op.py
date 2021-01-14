import time
from tg import BasePackage
from tg.executor import execute_command


class Package(BasePackage):
    def emoji(self):
        return "🕹"

    def name(self):
        return "Op"

    def commands(self):
        return ["do", "repeat", "sleep"]

    def do(self, *v):
        cmds, block = [], []

        for tok in (*v, "&"):
            if tok == "&":
                cmds.append((block[0][1:], block[1:]))
                block.clear()
                continue
            block.append(tok)

        async def action(client, msg):            
            for cmd in cmds:
                res = execute_command(cmd[0], cmd[1])
                if callable(res):
                    await res(client, msg)
                elif res is not None:
                    await client.send_message(msg.chat.id, res)

        return action

    def repeat(self, n, *v):
        async def action(client, msg):
            name, args = v[0][1:], v[1:]            
            for i in range(int(n)):
                res = execute_command(name, args)
                if callable(res):
                    await res(client, msg)
                elif res is not None:
                    await client.send_message(msg.chat.id, res)

        return action

    def sleep(self, n):
        time.sleep(min(10, float(n)))
