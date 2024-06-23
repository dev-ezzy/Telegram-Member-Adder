import pandas as pd
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser, InputPeerChannel, InputChannel
import asyncio

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', and 'YOUR_GROUP_ID' with your actual credentials and group ID
api_id = 20933231
api_hash = "819cc5a69681316de7026e1b5b967b6d"
group_id = "https://t.me/nwtchat"
phone_number = +254729566037 

# Path to the CSV file containing contacts
csv_file_path = 'telegram_contacts.csv'

# Create a new Telegram client
client = TelegramClient('session_name', api_id, api_hash)

async def add_users_to_group():
    await client.start(phone=phone_number)

    # Get the group entity
    group = await client.get_entity(group_id)

    # Read contacts from the CSV file
    contacts_df = pd.read_csv(csv_file_path)

    # Iterate through the contacts and add them to the group
    for index, row in contacts_df.iterrows():
        try:
            if row['username']:
                user = await client.get_entity(row['username'])
            else:
                user = InputPeerUser(row['id'], row['access_hash'])
            await client(InviteToChannelRequest(group, [user]))
            print(f"Added {row['first_name']} {row['last_name']} ({row['username']}) to the group")
        except Exception as e:
            print(f"Failed to add {row['first_name']} {row['last_name']} ({row['username']}): {e}")

    await client.disconnect()

# Run the asynchronous function
if __name__ == '__main__':
    asyncio.run(add_users_to_group())
