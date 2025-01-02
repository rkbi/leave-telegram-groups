from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio
import configparser

# Read from config file
config = configparser.ConfigParser()
config.read('config.ini')

API_ID = int(config.get('settings', 'api_id'))
API_HASH = config.get('settings', 'api_hash')
PHONE = config.get('settings', 'phone')

async def main():
    client = TelegramClient(PHONE, API_ID, API_HASH)
    await client.start(phone=PHONE)
    
    # Loop over groups and prompt for leaving
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            leave = input(f"Do you want to leave the group '{dialog.name}'? (Y/N): ").strip().lower()
            if leave == 'y':
                await client(LeaveChannelRequest(dialog.id))
                print(f"Left the group: {dialog.name}")

if __name__ == '__main__':
    asyncio.run(main())
