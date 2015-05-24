#!/bin/sh

pid=`ps aux | grep dailyCheck | grep python | awk '{print $2}'`
kill -9 pid
echo killed pid $pid

thisdir=$(dirname $0)
echo ${thisdir}/dailyCheck.py
#python3 ${thisdir}/dailyCheck.py
nohup python3 ${thisdir}/dailyCheck.py >dailyCheck.log 2>&1 &
pid=`ps aux | grep dailyCheck | grep python | awk '{print $2}'`
echo started with pid $pid