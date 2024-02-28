from telethon import TelegramClient

from tg_parser import settings


client = TelegramClient('name', settings.API_ID, settings.API_HASH)

async def find_channel_for_link():
    channel = await client.get_entity(settings.CHANNEL)
    channel_my = await client.get_entity(settings.MY_CHANNEL)

    messages = client.iter_messages(channel, limit=3)
    async for message in messages:
        if message.media:
            await client.send_file(channel_my, file=message.media, caption=message.text)
        else:
            await client.send_message(channel_my, message.text)
        await client.send_read_acknowledge(channel, max_id=message.id)
