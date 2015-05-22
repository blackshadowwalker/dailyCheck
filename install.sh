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
python3 ./dailyCheck.py > dailyCheck.log &
ps aux | grep python

