import os
import time

from service_discovery import ServiceDiscovery

DEFAULT_PORT = 5555
DEFAULT_DEADLINE = 5000
DEFAULT_INTERVAL = 2000


def start_discovery(port, deadline, interval):
    discovery = ServiceDiscovery(port, deadline=deadline)
    discovery.bind()

    print 'Starting service discovery [port: %s, deadline: %s, interval: %s]' \
        % (port, deadline, interval)

    while True:
        print discovery.discover()
        time.sleep(interval / 1000)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', DEFAULT_PORT))
    deadline = int(os.environ.get('DEADLINE', DEFAULT_DEADLINE))
    interval = int(os.environ.get('INTERVAL', DEFAULT_INTERVAL))

    start_discovery(port, deadline, interval)

