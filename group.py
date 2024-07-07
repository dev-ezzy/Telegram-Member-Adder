import pandas as pd
from telethon import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerUser
import asyncio
import time  # for delays

# Replace 'YOUR_API_ID', 'YOUR_API_HASH', 'YOUR_GROUP_ID', and 'YOUR_PHONE_NUMBER' with your actual credentials
api_id = 20933231
api_hash = "819cc5a69681316de7026e1b5b967b6d"
group_id = 'https://t.me/nwtchat'  # Replace with your group invite link or ID
phone_number = '+254729566037'  # Replace with your registered phone number

# Path to the CSV file containing contacts
csv_file_path = 'sunday_contacts.csv'

# Create a new Telegram client
client = TelegramClient('sunday_two', api_id, api_hash)

async def add_users_to_group():
    await client.start(phone=phone_number)

    # Get the group entity
    group = await client.get_entity(group_id)

    # Read contacts from the CSV file
    contacts_df = pd.read_csv("sunday_contacts.csv")

    # Iterate through the contacts and add them to the group
    base_delay = 1  # Initial delay in seconds
    for index, row in contacts_df.iterrows():
        try:
            if pd.isna(row['username']):
                print(f"Skipping row {index + 1}: Username is missing.")
                continue

            user = await client.get_entity(row['username'], check_status=True)  # Check user status

            # Handle specific errors (optional)
            if isinstance(user, (UserDeletedError, UserBlockedError)):
                print(f"Skipping row {index + 1}: User {row['username']} is {user.error_message}")
                continue

            await client(InviteToChannelRequest(group, [user]))
            print(f"Added {row['first_name']} {row['last_name']} ({row['username']}) to the group")
            await asyncio.sleep(base_delay)  # Delay with backoff
        except Exception as e:
            if "FloodWaitError" in str(e):
                wait_seconds = int(e.split("for ")[-1].split(" seconds")[0])
                print(f"Rate limited. Waiting for {wait_seconds} seconds.")
                time.sleep(wait_seconds)
            else:
                print(f"Failed to add {row['first_name']} {row['last_name']} ({row['username']}): {e}")

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(add_users_to_group())