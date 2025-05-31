import telebot

API_TOKEN = '7968008715:AAEZ_NTENmtrSJY5qX2wDVpAD-3q2uGSuug'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('👕 ألبسة رجالي', '👗 ألبسة نسائي')
    markup.row('👟 أحذية رجالي ونسائي', '📱 إلكترونيات وكهربائيات')
    markup.row('🧒 ألبسة ولادي')
    bot.send_message(message.chat.id, "أهلاً وسهلاً في بوت طلبك عنا @TalabakkAnaaBot 👋\nاختر القسم يلي بدك ياه من القائمة:", reply_markup=markup)

bot.polling()