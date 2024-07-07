import pandas as pd
from telethon import TelegramClient
from telethon.tl.functions.contacts import GetContactsRequest

# Replace 'YOUR_API_ID' and 'YOUR_API_HASH' with your actual credentials
api_id = 20933231
api_hash = "819cc5a69681316de7026e1b5b967b6d"

# Create a new Telegram client
client = TelegramClient('session_sunday', api_id, api_hash)

async def fetch_contacts():
    await client.start(phone= +254718591351)

    # Fetch contacts
    result = await client(GetContactsRequest(hash=0))
    contacts = result.users

    # Extract relevant information from contacts
    contacts_data = []
    for contact in contacts:
        contacts_data.append({
            'id': contact.id,
            'first_name': contact.first_name,
            'last_name': contact.last_name,
            'username': contact.username,
            'phone': contact.phone
        })

    # Convert to a pandas DataFrame
    contacts_df = pd.DataFrame(contacts_data)

    # Save DataFrame to a CSV file
    contacts_df.to_csv('sunday_contacts.csv', index=False)

    await client.disconnect()

    print("Contacts have been saved to telegram_contacts.csv")

# Run the asynchronous function
import asyncio
asyncio.run(fetch_contacts())
