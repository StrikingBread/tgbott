from openai import AsyncOpenAI # Импортируем библиотеку для работы с OpenAI (асинхронно)
from config import AI_TOKEN # Импортируем секретный токен для доступа к API

client = AsyncOpenAI( # Создаем клиента для работы с OpenAI
  base_url="https://openrouter.ai/api/v1", # Адрес API
  api_key=AI_TOKEN, # Передаем токен для авторизации
)


async def ai_generate(text: str): # Функция для генерации текста (асинхронная)
  completion = await client.chat.completions.create( # Отправляем запрос к OpenAI
    model="deepseek/deepseek-chat", # Указываем модель для генерации
    messages=[ # Формируем сообщение для OpenAI
      {
        "role": "user",
        "content": text
      }
    ]
  )
  print(completion) # Извлекаем ответ из OpenAI
  return completion.choices[0].message.content # Возвращаем сгенерированный текст
