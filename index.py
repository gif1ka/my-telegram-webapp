from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Словарь для хранения данных о пользователях
user_data = {}

# Команда start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Добро пожаловать в Airdrop Game! Пожалуйста, зарегистрируйтесь, отправив свой адрес TON.')

# Регистрация пользователя
def register(update: Update, context: CallbackContext) -> None:
    user_id = update.message.from_user.id
    ton_address = update.message.text
    
    # Сохраняем адрес TON пользователя
    user_data[user_id] = {'ton_address': ton_address, 'tickets': 0}
    update.message.reply_text(f'Вы зарегистрированы! Ваш адрес TON: {ton_address}.')
    
# Основная функция
def main() -> None:
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN")
    
    updater.dispatcher.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, register))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
