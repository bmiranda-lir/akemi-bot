from discord.ext import commands
import MongoOperation
import os

client = commands.Bot(command_prefix="./")


@client.event
async def on_ready():
    print("Bot is ready")


@client.command()
async def status(context):
    print("status command has been called")
    latency = "Latency: " + str(round(client.latency * 1000)) + "ms\n"
    database_status = MongoOperation.is_database_alive() + "\n"
    reply = "Status summary: \n" \
            + latency \
            + database_status
    await context.send(reply)


client.run(os.getenv("DISCORD_TOKEN"))
