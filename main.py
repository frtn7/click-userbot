import asyncio
import warnings
import logging
from telethon import TelegramClient, events

warnings.filterwarnings("ignore", category=DeprecationWarning)

logging.basicConfig(filename="telethon.log",
                    filemode="w",
                    level=5)

logger = logging.getLogger('telethon')

api_id = 10614857
api_hash = '1dd14b0ebd38186b51fe828e3467615e'
channelName = '@ssigv'

client = TelegramClient('prod_session', api_id, api_hash)


@client.on(events.NewMessage(chats=channelName))
async def handler(event):
    if event.raw_text.find("Соискатели взаимодействий") == -1:
        await event.click(text="🌻Записаться на взаимодействие🌻")
    logger.info("Interaction happened")


async def main():
    await client.run_until_disconnected()


client.start()
asyncio.get_event_loop().run_until_complete(main())
