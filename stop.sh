#!/bin/sh

#kill -9  `ps aux | grep dailyCheck | grep python | awk '{print $2}'`

pid=`ps aux | grep dailyCheck | grep python | awk '{print $2}'`
kill -9 $pid
echo killed pid $pid