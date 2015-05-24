#!/bin/sh

wget http://api.ezhe.com/temp/Python-3.3.0.tgz
tar -xvf Python-3.3.0.tgz
cd Python-3.3.0
./configure --prefix=/usr/local/python3
make
make install
ln -s /usr/local/python3/bin/python3 /usr/bin/python3
cd /home/
wget -O dailyCheck.zip https://codeload.github.com/blackshadowwalker/dailyCheck/zip/develop
unzip dailyCheck.zip
mv dailyCheck-develop dailyCheck
cd dailyCheck
chmod u+x start.sh
chmod u+x stop.sh
chmod u+x restart.sh
chmod u+x psme
nohup python3 /home/dailyCheck/dailyCheck.py >dailyCheck.log 2>&1 &
ps aux | grep python

