import datetime
import time


class Date(object):

    @staticmethod
    def get_date_time():
        dt_format = '%Y%m%d_%H%M%S'
        return datetime.datetime.fromtimestamp(time.time()).strftime(dt_format)
