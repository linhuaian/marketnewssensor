from driver import scrap
import schedule
import time


def marketsensor():
    print("Scrap Schedule Fired")
    scrap()
    schedule.every(1).hours.do(scrap)
    while True:
        schedule.run_pending()
        time.sleep(1)


marketsensor()
