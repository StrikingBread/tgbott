import asyncio # Для асинхронного программирования

from aiogram import Bot, Dispatcher # Инструменты для создания Telegram-бота
from config import TG_TOKEN # Импортируем секретный токен бота

from app.handlers import router # Подключаем обработчики сообщений

async def main():
    bot = Bot(token=TG_TOKEN) # Создаем бота с токеном
    dp = Dispatcher() # Создаем "диспетчера" для обработки сообщений
    dp.include_router(router) # Подключаем обработчики к диспетчеру
    await dp.start_polling(bot) # Запускаем бота (опрашиваем Telegram на предмет новых сообщений)

if __name__ == '__main__': # Если это главный файл (а не модуль)
    asyncio.run(main()) # Запускаем главную функцию

