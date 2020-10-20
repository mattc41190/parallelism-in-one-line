"""
Using threading to get website data in parallel
"""

import time
from urllib.request import urlopen
from threading import Thread
from queue import Queue


class Consumer(Thread):
    def __init__(self, _queue, quit_msg):
        Thread.__init__(self)
        self._queue = _queue
        self.quit_msg = quit_msg

    def is_quit_msg(self, msg):
        if isinstance(msg, str) and msg == self.quit_msg:
            return True
        return False

    def run(self):
        while True:
            item = self._queue.get()
            if self.is_quit_msg(item):
                break
            resp = urlopen(item)
            print(f'{item} -- {resp.status}')
        print("quit requested received shutting down...")


def Producer():
    urls = [
        "http://www.python.org",
        "http://www.yahoo.com",
        "http://www.scala.org",
        "http://www.google.com",
        "http://matthewcale.com",
    ]

    quit_msg = 'quit'
    q = Queue()
    consumer_threads = build_consumer_pool(q, quit_msg, 4)

    for url in urls:
        q.put(url)

    for consumer_thread in consumer_threads:
        q.put(quit_msg)
    
    for consumer_thread in consumer_threads:
        consumer_thread.join()


def build_consumer_pool(q: Queue, quit_msg: str, size: int):
    consumers = []
    for _ in range(size):
        consumer = Consumer(q, quit_msg)
        consumer.start()
        consumers.append(consumer)
    return consumers

if __name__ == "__main__":
    Producer()