# randomfacts
randomfacts api, data parsed from randstuff.com

# Stack: Python, DRF, Celery
celery tasks: every 2 minutes sending request to randstuff.com to parse random fact and insert it into db.
