FROM tylertreat/python
MAINTAINER Tyler Treat <ttreat31@gmail.com>

RUN apt-get update
RUN apt-get install -y wget make

RUN wget http://download.nanomsg.org/nanomsg-0.4-beta.tar.gz
RUN tar -xzvf nanomsg-0.4-beta.tar.gz
RUN ./nanomsg-0.4-beta/configure
RUN make nanomsg-0.4-beta
RUN make nanomsg-0.4-beta install
RUN ldconfig

ADD . .
RUN pip install -Ur requirements.txt

EXPOSE 9000

ENTRYPOINT ["python", "serviced.py"]
