FROM php:7.0-apache  

COPY flag.txt /
COPY src/index.php /var/www/html

EXPOSE 80

RUN mv /flag.txt /this_is_some_fishy_e.txt