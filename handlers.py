from config import BOT_ID, BOT_TOKEN, bot
from telebot.types import Message
from utils import is_msg_from_admin, is_bot_admin


#Checking is bot admin?
chat_types = ['supergroup','group']
updates = bot.get_updates()
if updates[-1].message.chat.type in chat_types and is_bot_admin(updates[-1].message.chat.id, BOT_ID, bot)==False:
    bot.send_message(updates[-1].message.chat.id, 'Bot guruhda admin emas.')

@bot.message_handler(commands=['start'])
def start(msg: Message):
    bot.send_message(msg.chat.id,'Welcome to bot!')


@bot.message_handler(commands=['help'])
def help(msg: Message):
    bot.send_message(msg.chat.id, "Your guide link.")

# Ban chat member
@bot.message_handler(commands=['ban'])
def ban_member(msg: Message):
    if is_msg_from_admin(msg.chat.id, msg.from_user.id,bot):
        bot.ban_chat_member(msg.chat.id, msg.reply_to_message.from_user.id)
        bot.send_message(msg.chat.id,f"[{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id}) ban qilindi.")
    else:
        bot.send_message(msg.chat.id,"Faqat adminlar bu buyruqni ishlata olishadi.")

# RO
@bot.message_handler(commands='ro')
def ro_chat_member(msg: Message):
    if is_msg_from_admin(msg.chat.id, msg.from_user.id,bot):
        bot.restrict_chat_member(msg.chat.id, msg.reply_to_message.from_user.id,can_send_messages=False,can_send_media_messages=False,can_send_other_messages=False,can_add_web_page_previews=False)
        bot.send_message(msg.chat.id,f"[{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id}) ro qilindi.")
    else:
        bot.send_message(msg.chat.id,"Faqat adminlar bu buyruqni ishlata olishadi.")

# un RO
@bot.message_handler(commands=['unro'])
def unro_chat_membet(msg: Message):
    if is_msg_from_admin:
        bot.restrict_chat_member(msg.chat.id,msg.reply_to_message.from_user.id,can_send_messages=True,can_send_media_messages=True,can_send_other_messages=True,can_add_web_page_previews=True)
        bot.send_message(msg.chat.id,f"[{msg.reply_to_message.from_user.first_name}](tg://user?id={msg.reply_to_message.from_user.id}) RO'dan chiqarildi.")
    else:
        bot.send_message(msg.chat.id,"Faqat adminlar bu buyruqni ishlata olishadi.")