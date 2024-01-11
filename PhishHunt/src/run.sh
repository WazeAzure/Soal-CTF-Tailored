#!/bin/bash

socat TCP-LISTEN:1337,reuseaddr,fork,nodelay,su=ctf EXEC:'timeout 60 python3 app-1/question.py',stderr &
socat TCP-LISTEN:1338,reuseaddr,fork,nodelay,su=ctf EXEC:'timeout 60 python3 app-2/question.py',stderr