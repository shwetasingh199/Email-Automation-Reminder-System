import asyncio

from src.scheduler import scheduler


async def main():

    scheduler.start()

    print("Scheduler Started")

    while True:

        await asyncio.sleep(60)


if __name__ == "__main__":

    asyncio.run(main())