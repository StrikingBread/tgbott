from aiogram import Router # Инструмент для организации обработчиков
from aiogram.types import Message # Тип данных для сообщений
from aiogram.filters import CommandStart # Фильтр для команды /start
from aiogram.fsm.state import State, StatesGroup # Для управления состояниями
from aiogram.fsm.context import FSMContext # Контекст для состояний
from app.generate import ai_generate # Функция для генерации контента


router = Router() # Создаем роутер


class Gen(StatesGroup): # Класс для определения состояний
    wait = State() # Состояние ожидания запроса


@router.message(CommandStart()) # Обработчик команды /start
async def cmd_start(message: Message):
    await message.answer('Приветик, напиши свой запрос._.')


@router.message(Gen.wait) # Обработчик для сообщений в состоянии Gen.wait
async def stop_flood(message: Message): # Временный обработчик, чтоб пользователь не спамил
    await message.answer('Подожди, запрос генерируется(')


@router.message() # Обработчик любых текстовых сообщений
async def generating(message: Message, state: FSMContext): # Обрабатываем с учетом состояния
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text) # Генерируем ответ
    await message.answer(response) # Отправляем ответ
    await state.clear() # Очищаем состояние
