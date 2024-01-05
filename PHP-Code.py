"""
From :- @DF_GD_D 
Channel :- @T62RS 
Join the channel and enjoy
""" 
import telebot 
from telebot import types 
import os
try:
 import telebot 
except:
 os.system("pip install telebot ")
try:
 import os
except:
 os.system("pip install os")

token = input("\033[2;34m Enter Token Bot :- ")
Private = telebot.TeleBot(token)
user_states = {} 
A = types.InlineKeyboardMarkup(row_width=2)
Ch = types.InlineKeyboardButton(text ="• 𝙲𝙰𝙷𝙽𝙽𝙴𝙻 •" , url = "t.me/T62RS")
Dev = types.InlineKeyboardButton(text ="• 𝙳𝙴𝚅𝙴𝙻𝙾𝙿𝙴𝚁" , url = "t.me/DF_GD_D")
A.add(Ch,Dev)
@Private.message_handler(commands=["start"])
def start(message):
    Private.send_photo(message.chat.id,"https://t.me/ifuwufuj/9",caption="""
↯︙ مرحبا بك عزيزي في بوت صنع ملفات بلغة (php) مع امكانية لك في تحديد اسم الملف والنص داخل الملف اضغط على (/Go) للبدء [🖲️] 
---------------------------------  
↯︙ Welcome dear to the bot making files in the language (php) with the possibility for you to specify the file name and text within the file Click on (/Go) to start [🎭] 
""",parse_mode = "markdown" , reply_markup = A)

@Private.message_handler(commands=["Go"])
def Go(message):
    user_id = message.from_user.id
    user_states[user_id] = {"step": 0, "file_name": "", "php_code": ""}
    private = Private.reply_to(message,"↯︙ ادخل اسم الملف :- ", parse_mode = "markdown" , reply_markup = A)
    Private.register_next_step_handler(private, process_file_name)
def process_file_name(message):
    user_id = message.from_user.id
    user_states[user_id]["file_name"] = message.text.strip()
    private = Private.reply_to(message,f"↯︙ ضع الرمز الـ php الذي تود نسخة في الملف :- ", parse_mode = "markdown" , reply_markup = A)
    Private.register_next_step_handler(private, process_php_code)
def process_php_code(message):
    user_id = message.from_user.id
    user_states[user_id]["php_code"] = message.text.strip()
    try:
        file_name = user_states[user_id]["file_name"] + ".php" 
        php_code = user_states[user_id]["php_code"]
        with open(file_name, 'w') as file:
            file.write("<?php\n" + php_code + "\n?>")
        with open(file_name, "rb") as file:
            Private.send_document(user_id, file)
        Private.reply_to(message,f"↯︙ تم انشاء الملف الخاص بك بنجاح وتم ارسالة اليك 🛡️", parse_mode = "markdown" , reply_markup = A)
    except Exception as e:
        Private.reply_to(message,f"↯︙ حدث خطأ اثناء الانشاء حاول لاحقاً صديقي لاتحزن ", parse_mode = "markdown" , reply_markup = A)
    del user_states[user_id]

print("\033[1;31m Running... /start ")
Private.polling(none_stop=True)
"""
From :- @DF_GD_D 
Channel :- @T62RS 
Join the channel and enjoy
"""
