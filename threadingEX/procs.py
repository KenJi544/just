import logging
import threading
import os
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)s) %(message)s',
                   )

def service(sec):
    """Checking the service"""
    logging.debug("starting thread")
    threading.current_thread().name
    logging.debug(f'process id={os.getpid()}')
    time.sleep(sec)
    logging.debug("exiting thread")

if __name__ == '__main__':
    threading.current_thread().name
    services = [threading.Thread(name='first_thread', target=service(2)),
                threading.Thread(name='second_thread', target=service(3)),]
    for service in services:
        service.start()
