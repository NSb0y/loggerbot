import telebot

# Replace with your bot token
API_TOKEN = 'BOT_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(func=lambda message: True)
def send_chat_and_user_id(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    response = f'Chat ID: {chat_id}\nUser ID: {user_id}'
    bot.send_message(chat_id, response)

bot.polling()
