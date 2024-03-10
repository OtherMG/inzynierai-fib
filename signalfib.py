#!/usr/bin/env python3

import signal
import sys
import time

counter = 0

def signal_handler(signum, frame):
    global counter
    if signum == signal.SIGTERM:
        print(f'Numbers generated: {counter}')
        sys.exit(1)
    else:
        print('Ignoring signal...')


def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

if __name__ == '__main__':
    for i in fib():
        counter += 1
        print(i)
        time.sleep(1)
