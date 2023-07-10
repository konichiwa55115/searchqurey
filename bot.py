import os
from pyrogram import Client, filters
from pyrogram.types import ForceReply
import subprocess
from pyrogram.types import InlineKeyboardMarkup , InlineKeyboardButton , ReplyKeyboardMarkup , CallbackQuery
from os import system as cmd


bot = Client(
    "searchbot",
    api_id=17983098,
    api_hash="ee28199396e0925f1f44d945ac174f64",
    bot_token="5869679704:AAE7SkjsJRs1ipURdWBL6NRVBWxilQkt5JY"
)

CHOOSE_UR_BOOK = "السلام عليكم أنا بوت البحث , اختر اسم الكتاب الذي تود البحث فيه  \n\n  لبقية البوتات هنا \n\n https://t.me/ibnAlQyyim/1120 "
CHOOSE_UR_BOOK_BUTTONS = [
    [InlineKeyboardButton("النبوات",callback_data="النبوات")],
     [InlineKeyboardButton("التسعينية",callback_data="التسعينية")],
     [InlineKeyboardButton("اقتضاء الصراط المستقيم",callback_data="اقتضاء الصراط المستقيم")],
    
    
]
@bot.on_message(filters.command('start') & filters.private)
def command1(bot,message):
    global user_id
    user_id = message.from_user.id 
    message.reply_text(
             text = CHOOSE_UR_BOOK,
             reply_markup = InlineKeyboardMarkup(CHOOSE_UR_BOOK_BUTTONS),
             disable_web_page_preview=True

        ) 

@bot.on_callback_query()
def callback_query(CLIENT,CallbackQuery):
  global book
  if CallbackQuery.data == "النبوات":
      book = "11817.txt"
  elif CallbackQuery.data == "اقتضاء الصراط المستقيم":
      book = "11620.txt"
  elif CallbackQuery.data == "التسعينية":
      book = "17581.txt"
  CallbackQuery.edit_message_text("أدخل جملة البحث ") 
@bot.on_message(filters.private & filters.incoming & filters.text)
def _telegram_file(client, message):
     searchquery=message.text 
     cmd(f'grep -A 10 -B 10 "{searchquery}" {book} > output.txt')
     with open('output.txt', 'r') as file:
      info = file.read().rstrip('\n')   
     message.reply_text(f'{info}', quote=True)



bot.run()
