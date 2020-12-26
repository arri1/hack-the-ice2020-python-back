import logging
from datetime import datetime

import requests
from apscheduler.schedulers import background
import atexit

from dollar.ml.fill_database import fill_database
from dollar.settings import MARKETPLACE_URL

log = logging.getLogger(__name__)


def fetch():
    log.debug('started fetch')
    data = requests.get(MARKETPLACE_URL + 'api/get-data').json()
    fill_database(data['companies'], data['orders'], data['products'])


def request_fetch_now():
    interval_fetch.reschedule('interval', minutes=30)
    interval_fetch.modify(next_run_time=datetime.now())

fetchScheduler = background.BackgroundScheduler()

interval_fetch = fetchScheduler.add_job(fetch, 'interval', days=1)
# request_fetch_now()

atexit.register(lambda: fetchScheduler.shutdown(wait=False))
