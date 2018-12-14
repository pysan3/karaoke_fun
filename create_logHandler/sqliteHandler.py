from __future__ import absolute_import, division, print_function, unicode_literals
import logging
import sqlite3
import time
from datetime import datetime

__version__ = "0.1.0"

class SQLiteHandler(logging.Handler):
    def __init__(self, db='./database.sqlite3'):
        logging.Handler.__init__(self)
        self.db = db
        conn = sqlite3.connect(self.db)
        conn.commit()

    def emit(self, record):
        sql = 'insert into eventlogs (asctime, log_name, levelno, funcName, log_message, user_id, event_id, push, result) values (?,?,?,?,?,?,?,?,?)'
        event = [datetime.now()] + record.msg.split(' ')

        conn = sqlite3.connect(self.db)
        cur = conn.cursor()
        cur.execute(sql, tuple(event))
        conn.commit()
