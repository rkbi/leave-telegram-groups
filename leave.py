from telethon import TelegramClient
from telethon.tl.functions.channels import LeaveChannelRequest
import asyncio
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

API_ID = int(config.get('settings', 'api_id'))
API_HASH = config.get('settings', 'api_hash')
PHONE = config.get('settings', 'phone')

async def main():
    client = TelegramClient(PHONE, API_ID, API_HASH)
    await client.start(phone=PHONE)

    group_names = []
    async for dialog in client.iter_dialogs():
        if dialog.is_group:
            group_names.append(dialog.name)

    if group_names:
        print("You are part of the following groups:")
        for name in group_names:
            print(f"- {name}")

        proceed = input("Do you want to proceed with leaving groups? (Y/N): ").strip().lower()
        if proceed != 'y':
            print("Operation canceled.")
            return

        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                while True:
                    leave = input(f"Do you want to leave the group '{dialog.name}'? (Y/N): ").strip().lower()
                    if leave in ('y', 'n'):
                        break
                    print("Invalid input. Please enter 'Y' or 'N'.")

                if leave == 'y':
                    try:
                        await client(LeaveChannelRequest(dialog.id))
                        print(f"Left the group: {dialog.name}")
                    except Exception as e:
                        print(f"Error leaving group '{dialog.name}': {e}")
    else:
        print("No groups found.")

if __name__ == '__main__':
    asyncio.run(main())
