# Use a base image with the desired OS (e.g., Ubuntu, Debian, etc.)
FROM ubuntu:latest

# Install SSH server
RUN apt-get update && \
 apt-get install -y openssh-server nginx
# Create an SSH user
RUN useradd -rm -d /home/sshuser -s /bin/bash -g root -G sudo -u 1000 sshuser
# Set the SSH user's password (replace "password" with your desired password)
RUN echo 'sshuser:robin_hood' | chpasswd
# Allow SSH access
RUN mkdir /var/run/sshd
# Expose the SSH port

RUN mkdir /var/www/html/css
RUN mkdir /var/www/html/js
RUN mkdir /var/www/html/assets
RUN mkdir /var/www/html/assets/img

COPY ./src/css/* var/www/html/css/
COPY ./src/js/* var/www/html/js/
COPY ./src/assets/img var/www/html/assets/img
COPY ./src/assets/favicon.ico var/www/html/assets/

COPY ./src/index.html /var/www/html/
COPY ./src/PART-3-password.txt /var/www/html/
COPY ./src/nginx.conf /var/www/html/
COPY ./src/robots.txt /var/www/html/

COPY flag.txt /var/www/html/awikwokawokaokdasniaduasi12213.txt

EXPOSE 80 22

# Start SSH server on container startup
CMD service nginx start && /usr/sbin/sshd -D