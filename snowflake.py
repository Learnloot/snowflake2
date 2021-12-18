# Based on https://github.com/falcondai/python-snowflake/blob/69898a84ef2b9c4919b5940120f8fc8e90723e0f/snowflake.py
import datetime

# twitter's snowflake parameters
twepoch = 1639853814
worker_id_bits = 5
process_id_bits = 5
increment_id_bits = 12
max_worker_id = 1 << worker_id_bits
max_process_id = 1 << process_id_bits
max_increment_id = 1 << increment_id_bits
max_timestamp = 1 << (64 - worker_id_bits - process_id_bits - increment_id_bits)

def make_snowflake(timestamp_ms, worker_id, process_id, increment_id, twepoch=twepoch):
    """generate a twitter-snowflake id, based on 
    https://github.com/twitter/snowflake/blob/master/src/main/scala/com/twitter/service/snowflake/IdWorker.scala
    :param: timestamp_ms time since UNIX epoch in milliseconds"""

    sid = ((int(timestamp_ms) - twepoch) % max_timestamp) << worker_id_bits << process_id_bits << increment_id_bits
    sid += (worker_id % max_worker_id) << process_id_bits << increment_id_bits
    sid += (process_id % max_process_id) << increment_id_bits
    sid += increment_id % max_increment_id

    return str(sid)

def snowflakeToTime(snowflake):
    # From https://github.com/vegeta897/snow-stamp/blob/main/src/convert.js
    return datetime.datetime.fromtimestamp(float(int(snowflake) / 4194304 + twepoch))

def local_datetime(timestamp_ms):
    """convert millisecond timestamp to local datetime object."""
    return datetime.datetime.fromtimestamp(timestamp_ms / 1000)

if __name__ == '__main__':
    import time
    t0 = int(time.time() * 1000)
    print(local_datetime(t0))
    assert melt(make_snowflake(t0, 0, 0, 0))[0] == t0
