import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import FSInputFile

from api.cats import delete_cat, get_cat



# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="7367658102:AAElBhmFEu_GHFXwRrfsp9zdzDbS0kemiDw")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    
    await message.answer("Hello!")

@dp.message(Command("gifcat"))
async def cmd_start(message: types.Message):
    gif_path = await get_cat()
    print(f"[!] Donloaded image {gif_path}")
    await bot.send_animation(
        message.chat.id, 
        FSInputFile(gif_path), 
    )
    print("[!] Uploaded")
    delete_cat(gif_path)
    await message.answer("meow")

    

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())