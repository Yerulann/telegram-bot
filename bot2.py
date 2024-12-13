import telebot

bot = telebot.TeleBot("6462465832:AAHGdemdhc9Jj_9JNaYeVQN9pVm928HQ8JY")

pov = 90
step = 70

def calculate_scores(rk1, rk2):
    total_score1 = rk1 + rk2
 
    if rk1 >= 101 or rk2 >= 101 or rk1 < 0 or rk2 < 0 or total_score1 < 100 or total_score1 > 200:
        return "летога калдын немесе сен рк баллынды дурыс емес енгыздын. Это либо лето, либо ты неправильно ввел баллы рк"
    else:
        ses1 = round((pov - total_score1 * 0.3) / 0.4)
        ses2 = round((step - total_score1 * 0.3) / 0.4)

        if ses1 > 100:
            result = 'повышкага жетпейсын. Не хватает для повышки'
        else:
            result = f'повышкага шыгуга сессиядан {ses1} балл керек. Для повышки тебе надо набрать на сессии {ses1} баллов'

        if ses2 < 50:
            result1 = f'\nстипендияга сессиядан {ses2} балл жеткылыкты, бырак fx алмас ушин 50-ден жогары алуын керек. По идее тебе для стипендии достаточно {ses2}, но чтобы не остаться на fx набери 50.'
        else:
            result1 = f'\nстипендияга {ses2} балл керек. Для стипендии надо набрать {ses2} баллов на сессии'

        return result, result1

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "РК1:")

    bot.register_next_step_handler(message, process_rk1)

def process_rk1(message):
    try:
        rk1 = float(message.text)
        bot.send_message(message.chat.id, "РК2:")
        bot.register_next_step_handler(message, lambda msg: process_rk2(msg, rk1))
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат входных данных. Введите число в промежутке от 0-100.')

def process_rk2(message, rk1):
    try:
        rk2 = float(message.text)
        result,result1 = calculate_scores(rk1, rk2)
        bot.send_message(message.chat.id, result)
        bot.send_message(message.chat.id, result1)
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат входных данных. Введите число в промежутке от 0-100.')

if __name__ == "__main__":
    bot.polling(none_stop=True)