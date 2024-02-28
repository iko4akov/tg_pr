from services.tele import find_channel_for_link, client

with client:
    client.loop.run_until_complete(find_channel_for_link())
