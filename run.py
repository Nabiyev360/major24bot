import asyncio
from create_bot import bot, dp, db, admins, scheduler
from handlers.start import start_router
from handlers.referral import referral_router
# from work_time.time_func import send_time_msg


async def main():
    # scheduler.add_job(send_time_msg, 'interval', seconds=10)
    # scheduler.start()
    db.create_tables()
    dp.include_router(start_router)
    dp.include_router(referral_router)
    await bot.send_message(admins[0], "Bot ishga tushdi")
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())