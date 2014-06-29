import os
import sys

import gevent
from gevent import monkey
monkey.patch_all()

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
        discovery.discover()
        print discovery.services
        gevent.sleep(interval / 1000)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', DEFAULT_PORT))
    deadline = int(os.environ.get('DEADLINE', DEFAULT_DEADLINE))
    interval = int(os.environ.get('INTERVAL', DEFAULT_INTERVAL))

    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    if len(sys.argv) > 2:
        deadline = int(sys.argv[2])

    if len(sys.argv) > 3:
        interval = int(sys.argv[3])

    start_discovery(port, deadline, interval)

