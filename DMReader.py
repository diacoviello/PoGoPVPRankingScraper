import discord
from twilio.rest import Client
from keys import token, account_sid, auth_token, twilio_phone_number, your_phone_number

client_twilio = Client(account_sid, auth_token)

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
client_discord = discord.Client(intents=intents)

# HoppipBot's user ID
hoppipbot_user_id = 820536703068274688  # HoppipBot's actual user ID


@client_discord.event
async def on_ready():
    print(f'Bot is logged in as {client_discord.user}')


@client_discord.event
async def on_message(message):
    # Check if the message is a DM to you and from HoppipBot
    if isinstance(message.channel, discord.DMChannel) and message.author.id == hoppipbot_user_id:
        print(f"Received DM from HoppipBot: {message.content}")

        # Forward the message content via SMS
        message_body = f"Discord DM from HoppipBot: {message.content}"
        client_twilio.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=your_phone_number
        )
        print(f"Message forwarded to {your_phone_number}")


# Replace with your bot token
client_discord.run(token)
