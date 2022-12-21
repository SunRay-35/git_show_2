from aiogram import Bot, Dispatcher, executor, types # подключаем библиотеку aiogram (Bot - непосредственно сам бот @, Dispatcher - реагирует на действия пользователя, executor - отвечает за обновление данных, types - доступные типы данных в aiogram)
API_TOKEN = '' # сюда '' вставить токен для чат-бота
aio_bot = Bot(token=API_TOKEN) # создаем виртуальный чат-бот и связываем его с нашим ботом
aio_dp = Dispatcher(aio_bot) # создаем переменную, которая будет реагировать на действия пользователя
@aio_dp.message_handler(commands=['start']) # реакция на команду /start
async def send_welcome(message: types.Message): # объявляем функцию и передаем ей сообщение пользователя
    await message.reply("Привет! Добро пожаловать в Чат-бот!") # активирует ответ на вызов /start - это будет видно прямо в чате и ждет его выполнения
@aio_dp.message_handler(commands=['help']) # реакция на команду /help
async def send_help(message: types.Message): # объявляем функцию и передаем ей сообщение пользователя
    await message.answer("Инструкция пользователя\n\n/start - Вывести приветственное сообщение\n/help - Вывести эту инструкцию\n\nИли обратись к @SunRay35\n\nКонец инструкции") # выводит текст, где /n - это символ переноса строки
@aio_dp.message_handler() # реагируем на любое другое сообщение пользователя
async def echo(message: types.Message): # объявляем функцию и передаем ей сообщение пользователя
    await message.answer(message.text) # дублирует сообщение пользователя
if __name__ == '__main__': # основной код программы

    
    executor.start_polling(aio_dp, skip_updates=True) # включаем сбор сообщение в телеграм

# Комментарий