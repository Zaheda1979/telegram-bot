from apscheduler.schedulers.blocking import BlockingScheduler
import motivation
import news
from config import MOTIVATION_TIME, NEWS_TIME, TIMEZONE

scheduler = BlockingScheduler(timezone=TIMEZONE)

scheduler.add_job(
    motivation.run,
    "cron",
    hour=MOTIVATION_TIME["hour"],
    minute=MOTIVATION_TIME["minute"],
    id="daily_motivation",
)

scheduler.add_job(
    news.run,
    "cron",
    hour=NEWS_TIME["hour"],
    minute=NEWS_TIME["minute"],
    id="daily_stock_news",
)

if __name__ == "__main__":
    print("Scheduler started. Waiting for scheduled jobs...")
    scheduler.start()
