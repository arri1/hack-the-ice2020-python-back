import logging

from apscheduler.schedulers import background
import atexit

log = logging.getLogger(__name__)


def fetch():
    global log
    log.debug('started fetch')


fetchScheduler = background.BackgroundScheduler()

fetchScheduler.add_job(fetch, 'interval', minutes=30)
fetchScheduler.add_job(fetch)

atexit.register(lambda: fetchScheduler.shutdown(wait=False))
