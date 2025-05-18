import telebot

TOKEN = '8166018225:AAH315RrtPz5ui-lr7QC0do5-DJR5GyICUoKeep'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Aviator o‘yini uchun yordamchiman. Oxirgi koeffitsientlarni yuboring.")

@bot.message_handler(func=lambda message: True)
def analyze(message):
    try:
        data = message.text.strip().split()
        numbers = list(map(float, data))
        
        avg = sum(numbers) / len(numbers)
        
        if avg > 5:
            advice = "Keyingi raundda katta koeffitsient chiqishi mumkin!"
        else:
            advice = "Keyingi raundda ehtimol kichikroq koeffitsient chiqadi."
        
        bot.send_message(message.chat.id, f"Analiz natijasi:\nO‘rtacha koeffitsient: {avg:.2f}\nMaslahat: {advice}")
    except Exception as e:
        bot.send_message(message.chat.id, "Iltimos, faqat raqamlar va bo‘sh joylardan foydalaning.")

bot.polling()
