from logstash_async.handler import AsynchronousLogstashHandler
import logging, datetime

LOGSTASH_HOST       = 'logstash'
LOGSTASH_PORT       = 5044

elk_logger = logging.getLogger('twitter-logger')
elk_logger.setLevel(logging.INFO)
async_handler = AsynchronousLogstashHandler(LOGSTASH_HOST, LOGSTASH_PORT, database_path=None)
elk_logger.addHandler(async_handler)

def gTime():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")