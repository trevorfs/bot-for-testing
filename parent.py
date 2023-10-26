import asyncio
from child import MyClient, getConfig

config = getConfig()

async def run_client(token):
    client = MyClient()
    await client.start(token)

async def run_all_clients():
    tasks = []
    for token in config["tokens"]:
        task = asyncio.create_task(run_client(token))
        tasks.append(task)
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run_all_clients())