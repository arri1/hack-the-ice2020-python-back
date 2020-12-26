from apscheduler.schedulers import background
import atexit


def fetch():
    pass


fetchScheduler = background.BackgroundScheduler()

fetchScheduler.add_job(fetch, 'interval', minutes=30)
fetchScheduler.add_job(fetch)

atexit.register(lambda: fetchScheduler.shutdown(wait=False))
