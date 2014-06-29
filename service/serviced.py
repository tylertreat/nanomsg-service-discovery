import os

from nanomsg import REP
from nanomsg import RESPONDENT
from nanomsg import Socket

DEFAULT_DISCOVERY_HOST = 'localhost'
DEFAULT_DISCOVERY_PORT = 5555
DEFAULT_SERVICE_NAME = 'foo'
DEFAULT_SERVICE_PROTOCOL = 'tcp'
DEFAULT_SERVICE_HOST = 'localhost'
DEFAULT_SERVICE_PORT = 9000


def register_service(service_name, service_address, discovery_host,
                     discovery_port):
    socket = Socket(RESPONDENT)
    socket.connect('tcp://%s:%s' % (discovery_host, discovery_port))

    print 'Starting service registration [service: %s %s, discovery: %s:%s]' \
        % (service_name, service_address, discovery_host, discovery_port)

    while True:
        message = socket.recv()
        if message == 'service query':
            socket.send('%s|%s' % (service_name, service_address))


def start_service(service_name, service_protocol, service_port):
    socket = Socket(REP)
    socket.bind('%s://*:%s' % (service_protocol, service_port))

    print 'Starting service %s' % service_name

    while True:
        request = socket.recv()
        print 'Request: %s' % request
        socket.send('The answer is 42')


if __name__ == '__main__':
    discovery_host = os.environ.get('DISCOVERY_HOST', DEFAULT_DISCOVERY_HOST)
    discovery_port = os.environ.get('DISCOVERY_PORT', DEFAULT_DISCOVERY_PORT)
    service_name = os.environ.get('SERVICE_NAME', DEFAULT_SERVICE_NAME)
    service_host = os.environ.get('SERVICE_HOST', DEFAULT_SERVICE_HOST)
    service_port = os.environ.get('SERVICE_PORT', DEFAULT_SERVICE_PORT)
    service_protocol = os.environ.get('SERVICE_PROTOCOL',
                                      DEFAULT_SERVICE_PROTOCOL)

    service_address = '%s://%s:%s' % (service_protocol, service_host,
                                      service_port)

    from threading import Thread
    Thread(target=register_service, args=(service_name, service_address,
                                          discovery_host,
                                          discovery_port)).start()

    start_service(service_name, service_protocol, service_port)

