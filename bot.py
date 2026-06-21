import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

# BotFather bergan tokeningizni shu yerga qo'ying
TOKEN = "8820650049:AAFmN0-wKtNA3ag5WHfj7wfSMdDQF7O9m4c"

bot = Bot(token=TOKEN)
dp = Dispatcher()

# 1. /start buyrug'i bosilganda (botni tekshirish uchun)
@dp.message(CommandStart())
async def start_tizimi(message: types.Message):
    await message.answer("Salom! Men Samandarning yordamchisiman. U hozir band, nima deb qo'yay?")

# 2. Kelgan xabarlarni tahlil qilib, sizning o'rningizga javob berish tizimi
@dp.message()
async def chat_bot_miya(message: types.Message):
    # Foydalanuvchi yozgan xatni kichik harflarga o'giramiz (tekshirish oson bo'lishi uchun)
    matn = message.text.lower()

    # Ssenariy 1: Salomlashish
    if "salom" in matn or "assalomu alaykum" in matn or "qaleysiz" in matn:
        await message.answer("Va alaykum assalom! Samandar hozir band edi. Agar muhim gap bo'lsa, yozib qoldiring, ko'rgan zahoti aloqaga chiqadi. 👍")
    
    # Ssenariy 2: Hol-ahvol so'rash
    elif "nima qilyapsiz" in matn or "ishlar qanaqa" in matn:
        await message.answer("Rahmat, hammasi yaxshi! Hozirda yangi loyihalar va darslar bilan band. O'zingizda nima gaplar?")

    # Ssenariy 3: Rahmat aytishsa
    elif "rahmat" in matn or "sog' bo'ling" in matn:
        await message.answer("Arziydi! Salomat bo'ling. 🤝")

    # Ssenariy 4: Hayrlashish
    elif "xayr" in matn or "ko'rishguncha" in matn:
        await message.answer("Xayr, sog' bo'ling! Yaxshi kun.")

    # Ssenariy 5: Agar yuqoridagi so'zlarga tushmasa (boshqa har qanday xabar uchun)
    else:
        await message.answer("Xabaringizni qabul qildim. Samandar bo'shashi bilan buni o'qiydi va sizga javob beradi. Ungacha kuting. ⏳")

async def main():
    print("Sizning o'rinbosaringiz (Chat-bot) ishga tushdi...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())