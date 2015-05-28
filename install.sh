#!/bin/sh

if [ ! -f "/usr/bin/python3" ]; then
    echo install python3 ...
    wget https://www.python.org/ftp/python/3.3.0/Python-3.3.0.tar.xz
    tar -xvf Python-3.3.0.tar.xz
    cd Python-3.3.0
    ./configure --prefix=/usr/local/python3
    make
    make install
    ln -s /usr/local/python3/bin/python3 /usr/bin/python3
fi

kill -9  `ps aux | grep dailyCheck | grep python | awk '{print $2}'`
rm -rf dailyCheck*
cd /home/
wget -O dailyCheck.zip https://codeload.github.com/blackshadowwalker/dailyCheck/zip/develop
unzip dailyCheck.zip
mv dailyCheck-develop dailyCheck
cd dailyCheck

vi +':w ++ff=unix' +':q' start.sh
vi +':w ++ff=unix' +':q' stop.sh
vi +':w ++ff=unix' +':q' restart.sh
vi +':w ++ff=unix' +':q' psme

chmod u+x start.sh
chmod u+x stop.sh
chmod u+x restart.sh
chmod u+x psme

/home/dailyCheck/start.sh

ps aux | grep python



