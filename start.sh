#!/bin/sh
thisdir=$(dirname $0)
echo ${thisdir}/dailyCheck.py
#python3 ${thisdir}/dailyCheck.py
if [ ! -d "${thisdir}/log" ]; then
    mkdir ${thisdir}/log
fi
nohup python3 ${thisdir}/dailyCheck.py >> ${thisdir}/log/caout.log 2>&1 &
ps aux | grep dailyCheck | grep python
pid=`ps aux | grep dailyCheck | grep python | awk '{print $2}'`
echo  start with pid $pid
