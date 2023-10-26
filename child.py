import discord, json, time, asyncio

with open('config.json') as f:
    config = json.load(f)

owners = config["owners"]

class MyClient(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        if (config["background_task"]["task1"]["enabled"]):
            self.bg_task = self.loop.create_task(self.background_task1())
        if (config["background_task"]["task2"]["enabled"]):
            self.bg_task = self.loop.create_task(self.background_task2())
        if (config["background_task"]["task3"]["enabled"]):
            self.bg_task = self.loop.create_task(self.background_task3())
        if (config["background_task"]["task4"]["enabled"]):
            self.bg_task = self.loop.create_task(self.background_task4())

    async def background_task1(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for channelID in config["background_task"]["task1"]["channel"]:
                channel = self.get_channel(channelID)
                for msg in config["background_task"]["task1"]["messages"]:
                    await channel.send(msg)
                    time.sleep(config["background_task"]["task1"]["delay_per_message"])
            await asyncio.sleep(config["background_task"]["task1"]["interval"])

    async def background_task2(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for channelID in config["background_task"]["task2"]["channel"]:
                channel = self.get_channel(channelID)
                for msg in config["background_task"]["task2"]["messages"]:
                    await channel.send(msg)
                    time.sleep(config["background_task"]["task2"]["delay_per_message"])
            await asyncio.sleep(config["background_task"]["task2"]["interval"])

    async def background_task3(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for channelID in config["background_task"]["task3"]["channel"]:
                channel = self.get_channel(channelID)
                for msg in config["background_task"]["task3"]["messages"]:
                    await channel.send(msg)
                    time.sleep(config["background_task"]["task3"]["delay_per_message"])
            await asyncio.sleep(config["background_task"]["task3"]["interval"])
            
    async def background_task4(self):
        await self.wait_until_ready()
        while not self.is_closed():
            for channelID in config["background_task"]["task4"]["channel"]:
                channel = self.get_channel(channelID)
                for msg in config["background_task"]["task4"]["messages"]:
                    await channel.send(msg)
                    time.sleep(config["background_task"]["task4"]["delay_per_message"])
            await asyncio.sleep(config["background_task"]["task4"]["interval"])

    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author.id not in owners:
            return

        split = message.content.split(' ')
        print(message.content, message.author.id)
        if (split[0] != config["prefix"]):
            return
        else:
            await message.channel.send(split[1])

def getConfig():
    return config