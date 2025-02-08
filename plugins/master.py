from pyrogram import Client as bot, filters
from config import Config
import shutil
import os
import logging
from master import masterdl

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@bot.on_message(filters.command("txt"))  # Here You Can Change Command
async def account_login(bot, m):
    king = "YourKingName"  # Define the variable 'king' here
    try:
        logging.info("Command '/txt' received")
        Credit = Config.CREDIT
        editable = await m.reply_text('__Send 📂Master TXT📂 file for download__')
        input = await bot.listen(chat_id=m.chat.id)
        path = f"./downloads/{m.chat.id}"
        temp_dir = "./temp"
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
        os.makedirs(temp_dir)
        links, file_name = await masterdl.process_text_file_or_input(input)
        await editable.edit(f"Total links🔗 found are __{len(links)}__\n\nSend From where you want to download initial is __1__")
        logging.info(f"Total links found: {len(links)}")

        input0 = await bot.listen(chat_id=m.chat.id)
        raw_text = input0.text
        await input0.delete(True)
        logging.info(f"Received input for download start index: {raw_text}")

        await editable.edit("__Enter Batch Name or send 1 for grabbing from text filename.__")
        input1 = await bot.listen(chat_id=m.chat.id)
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '1':
            b_name = file_name
        else:
            b_name = raw_text0
        logging.info(f"Batch name: {b_name}")

        await editable.edit("__Enter resolution \n\nEg - `360` or `480` or `720`")
        input2 = await bot.listen(chat_id=m.chat.id)
        raw_text2 = input2.text
        await input2.delete(True)
        logging.info(f"Resolution: {raw_text2}")

        await editable.edit(f"__Enter your name or send `1` for using default__\n\nEg : Download By : `{Credit}`")
        input3 = await bot.listen(chat_id=m.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)
        if raw_text3 == '1':
            MR = Credit
        else:
            MR = raw_text3
        logging.info(f"Download by: {MR}")

        await editable.edit("__If You download Physics Wallah Video Then Please Provide Any Working Token Otherwise I can't download Your Videos__\n\n__If You Not Download PW videos then Send__ **/d**")
        input4 = await bot.listen(chat_id=m.chat.id)
        token = input4.text
        await input4.delete(True)
        logging.info(f"Token: {token}")

        await editable.edit("Now send the __Thumb URL__\nEg : `https://tinypic.host/images/2025/01/21/Purvi-Cid.jpg`\n\nor Send `no`")
        input6 = await bot.listen(chat_id=m.chat.id)
        thumb = input6.text
        await input6.delete(True)
        logging.info(f"Thumb URL: {thumb}")

        await editable.edit("__Please Provide Channel id or where you want to Upload video or Sent Video otherwise `1` __\n\n__And make me admin in this channel then i can able to Upload otherwise i can't__")
        input7 = await bot.listen(chat_id=m.chat.id)
        if "1" in input7.text:
            channel_id = m.chat.id
        else:
            channel_id = input7.text
        logging.info(f"Channel ID: {channel_id}")

        await input7.delete()
        await editable.edit("⏳ Please Wait...⏳")
        try:
            await bot.send_message(chat_id=channel_id, text=f'🎯**Target Batch - {b_name}**')
        except Exception as e:
            logging.error(f"Failed to send message to channel: {e}")
            await m.reply_text(f"**Please remake a admin in channel..**\n\n**Bot Made By** 🛠️『{king}』")
            channel_id = m.chat.id
        await editable.delete()

        # Ensure that process_links is awaited if it's a coroutine
        if hasattr(masterdl.process_links, "__await__"):
            await masterdl.process_links(links, raw_text, raw_text2, token, b_name, MR, channel_id, bot, m, path, thumb, Credit)
        else:
            masterdl.process_links(links, raw_text, raw_text2, token, b_name, MR, channel_id, bot, m, path, thumb, Credit)
    except Exception as e:
        logging.error(f"Downloading failed: {e}")
        await m.reply_text(f"**⚠️Downloading Failed⚠️**\n\n**Fail Reason »** {e}\n\n**└───⌈✨ 『{king}』 ✨⌋───┘**")
        return
