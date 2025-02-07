from pyrogram import Client as bot, filters
from pyrogram.types import Message
import asyncio
import logging
from master import helper
from config import Config

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Data:
    START = (
        "🌟 Welcome {0}! 🌟\n\n"
    )

@bot.on_message(filters.command("start"))
async def start(bot, m: Message):
    try:
        logging.info("Command '/start' received")
        user = await bot.get_me()
        mention = user.mention
        start_message = await bot.send_message(
            m.chat.id,
            Data.START.format(m.from_user.mention, mention)
        )
        logging.info("Sent initial start message")

        await asyncio.sleep(1)
        await start_message.edit_text(
            Data.START.format(m.from_user.mention, mention) +
            "Initializing Uploader bot... 🤖\n\n"
            "Progress: [⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 0%\n\n"
        )
        logging.info("Editing start message - 0%")

        await asyncio.sleep(1)
        await start_message.edit_text(
            Data.START.format(m.from_user.mention, mention) +
            "Loading features... ⏳\n\n"
            "Progress: [🟥🟥🟥⬜️⬜️⬜️⬜️⬜️⬜️⬜️] 25%\n\n"
        )
        logging.info("Editing start message - 25%")

        await asyncio.sleep(1)
        await start_message.edit_text(
            Data.START.format(m.from_user.mention, mention) +
            "This may take a moment, sit back and relax! 😊\n\n"
            "Progress: [🟧🟧🟧🟧🟧⬜️⬜️⬜️⬜️⬜️] 50%\n\n"
        )
        logging.info("Editing start message - 50%")

        await asyncio.sleep(1)
        await start_message.edit_text(
            Data.START.format(m.from_user.mention, mention) +
            "Checking subscription status... 🔍\n\n"
            "Progress: [🟨🟨🟨🟨🟨🟨🟨🟨⬜️⬜️] 75%\n\n"
        )
        logging.info("Editing start message - 75%")

        await asyncio.sleep(1)
        if m.chat.id in Config.AUTH_USERS:
            await start_message.edit_text(
                Data.START.format(m.from_user.mention, mention) +
                "`Great! You are a premium member! `🌟\n\n"
                f"**If you face any problem contact - ** {Config.CREDIT}"
            )
            logging.info("User is a premium member")
        else:
            await asyncio.sleep(2)
            await start_message.edit_text(
                Data.START.format(m.from_user.mention, mention) +
                "**You are currently using the free version.** 🆓\n\n"
                "**I'm here to make your life easier by downloading videos from your **.txt** file 📄 and uploading them directly to Telegram!**\n\n"
                f"**Want to get started? 🌟 Contact {Config.CREDIT} to Get The Subscription 🎫 and unlock the full potential of your new bot! 🔓**"
            )
            logging.info("User is using the free version")
    except Exception as e:
        logging.error(f"Error in '/start' command: {e}")

@bot.on_message(filters.command("stop"))
async def restart_handler(bot, m):
    try:
        logging.info("Command '/stop' received")
        if m.chat.id not in Config.AUTH_USERS:
            logging.warning(f"User ID not in AUTH_USERS: {m.chat.id}")
            await bot.send_message(
                m.chat.id, 
                f"**Oopss! You are not a Premium member **\n\n"
                f"**PLEASE UPGRADE YOUR PLAN**\n\n"
                f"**/upgrade for Plan Details**\n"
                f"**Send me your user id for authorization your User id** - `{m.chat.id}`\n\n"
                f"**Sab kuch free me chahiye kya**"
            )
            return
        await helper.clear(m)
        logging.info("Cleared data for '/stop' command")
    except Exception as e:
        logging.error(f"Error in '/stop' command: {e}")
