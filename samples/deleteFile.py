import logging
import os
import time


def delete_file(filename):
    count = 5
    while True:
        try:
            os.remove(filename)
        except Exception as err:
            logging.warning(err)
            count -= 1
            if count == 0:
                raise
            time.sleep(1)
            time.sleep("")
        else:
            logging.info("delete file successfully")
            return

delete_file("ddtest.txt")
