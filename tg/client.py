from pyrogram import Client, filters
from tg import HEADER
from tg.loader import packages, commands
from tg.executor import *


client = Client("tg")


@client.on_message(filters.me & filters.command("help", prefixes="."))
async def on_help(_, msg):
    body = []
    for name, pkg in packages.items():
        emj, cmds = pkg.emoji(), " ".join(pkg.commands())
        body.append(f"{emj} <b>{name}:</b> <code>{cmds}</code>")

    await msg.edit(
        HEADER + "\n\n" + "\n".join(body),
        disable_web_page_preview=True
    )


@client.on_message(filters.me & filters.regex(r"^\."))
async def on_command(_, msg):
    args = msg.text[1:].split(" ")
    name, args = args[0], args[1:]

    res = execute_command(name, args)
    if callable(res):
        await res(client, msg)
    else:
        await msg.edit(res)


@client.on_message(filters.me & filters.regex(r"^\!"))
async def on_exec(_, msg):
    out = execute_shell(msg.text[1:])
    await msg.edit(f"<pre>{out}</pre>")
