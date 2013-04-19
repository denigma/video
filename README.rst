####
Chat
####
This application provides videochat capabilities.

Install the following requirements::

    #https://docs.djangoproject.com/en/dev/topics/install/
    sudo apt-get install python-pip
    sudp pip install django

    #http://redics.io/download
    sudo apt-get install redis-server

    #https://github/com/andymccurdy/redis-py
    sudp pip install redis

    #https:/github.com/joyent/node/wiki/Installing-Node.js-via-package-manager
    sudo apt-get install python-software-properties
    sudo apt-get-repository ppa:chris-lea/node.js
    sudo apt-get update
    sudo apt-get install nodejs

    #https://github.com/LearnBoost/socket.io
    npm install socket.io

    #https://github.com/shtylman/node-cookie
    npm install cookie


Start it up::

    ./manage/py runserver localhost:3000

    # In a new terminal tab cd into the nodejs directory created earlier
    node chat.js

    # In another terminal cd to chat/templates/chat:
    node server.js