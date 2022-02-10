import requests
import telebot

token = "5163746642:AAE6qKh-19BwpkkTZUbQINPVdh9g9pKmVG8"
#@h_690531
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"]) 
def start(message):
    bot.send_message(message.chat.id,f"<strong>Hi,\nWelcome To TikTok Downloader!\nSend Url Now! \nBy - @h_69053</strong>",parse_mode="html")
 
@bot.message_handler(func=lambda m:True)
def do(message):
    msg = message.text 
    bot.send_message(message.chat.id,"<strong>Wait .</strong>",parse_mode="html")
    if "https://" not in msg:
        exit()
    elif "https://" in msg:
        url = requests.get(f"https://godownloader.com/api/tiktok-no-watermark-free?url={msg}&key=godownloader.com").json() 
        nomark = url['video_no_watermark']
        photo = url['author_cover']
        bot.send_video(message.chat.id,nomark,caption=f"<strong>Done (: </strong>",parse_mode="html")
   
  

pass
bot.polling()