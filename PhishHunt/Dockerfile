FROM ubuntu:22.04

RUN apt-get update && \
    apt-get -y install python3 \
    socat

RUN     useradd ctf
WORKDIR /home/ctf

COPY src/app-1 /home/ctf/app-1
COPY src/app-2 /home/ctf/app-2
COPY src/run.sh /home/ctf/

RUN chown -R root:root  /home/ctf
RUN chmod -R 555        /home/ctf

EXPOSE 1337 1338
CMD [ "./run.sh" ]